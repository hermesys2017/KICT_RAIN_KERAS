import os
from abc import ABC, abstractmethod

import numpy as np
import tensorflow as tf
from tensorflow.lite.python.interpreter import Interpreter


class RainModel(ABC):
    model = None

    @abstractmethod
    def load_model(self, path):
        pass

    @abstractmethod
    def prediction(self, input_data):
        pass

    @abstractmethod
    def save_prediction_files(self, input_data, folder_path):
        prediction = self.prediction(input_data)
        self.save_as_ascii_grid(prediction, folder_path)

    def create_folder_recursive(self, folder_path):
        os.makedirs(folder_path, exist_ok=True)

    def rain(self, array):
        R = array * 255.0
        return R

    def CSI_m(self, y_true, y_pred):
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        y_true = y_true.reshape(1, -1)[0]
        y_pred = y_pred.reshape(1, -1)[0]
        remove_NAs = y_true > 0
        y_true = np.where(y_true[remove_NAs] >= 0.1, 1, 0)
        y_pred = np.where(y_pred[remove_NAs] >= 0.1, 1, 0)
        right = np.sum(y_true * y_pred == 1)
        # print(right,np.sum(y_pred),np.sum(y_true),right)
        CSI = right / (np.sum(y_pred) + np.sum(y_true) - right + 1e-07)
        return CSI

    def CSI_custom(self, y_true, y_pred):
        score = tf.py_function(
            func=self.CSI_m, inp=[y_true, y_pred], Tout=tf.float32, name="CSI_custom"
        )
        return score

    def mae_custom(self, y_true, y_pred):
        y_pred = tf.convert_to_tensor(y_pred)
        y_true = tf.convert_to_tensor(y_true)
        y_true = self.rain(y_true)
        y_pred = self.rain(y_pred)
        thr1 = K.greater(y_true, 0.1)
        loss1 = K.mean(K.abs(y_true[thr1] - y_pred[thr1]))
        arr = [loss1]
        value_not_nan = tf.dtypes.cast(
            tf.math.logical_not(tf.math.is_nan(arr)), dtype=tf.float32
        )
        loss0 = tf.math.multiply_no_nan(arr, value_not_nan)
        loss = tf.convert_to_tensor(K.sum(loss0))
        return loss

    def data_postprocessing(self, nwcst):
        # 0. Squeeze empty dimensions
        nwcst = np.squeeze(np.array(nwcst))
        nwcst = nwcst
        nwcst = np.where(nwcst > 0, nwcst, 0)
        nwcst = nwcst[7:632, 9:534]
        return nwcst

    def save_as_ascii_grid(self, data, output_file):
        """
        2D NumPy array를 ASCII grid 파일로 저장하는 함수
        :param data: 2D NumPy array (격자 자료)
        :param output_file: 저장할 파일 경로 및 이름 (예: 'output.asc')
        """
        # EPSG 5186 기준
        nrows, ncols = data.shape
        header = f"ncols {ncols}\n"
        header += f"nrows {nrows}\n"
        header += "xllcorner -31000\n"
        header += "yllcorner 123000\n"
        header += "cellsize 1000.0\n"  # 셀 크기
        header += "NODATA_value -9999.0\n"  # 누락된 데이터를 나타내는 값

        np.savetxt(
            output_file, data, fmt="%.2f", header=header, comments="", delimiter=" "
        )


class RainVer1Model(RainModel):
    def __init__(self, path: str):
        self.model = self.load_model(path)

    def save_prediction_files(self, input_data: np.ndarray, output_folder_path: str):
        self.create_folder_recursive(output_folder_path)
        prediction = self.prediction(input_data)
        for j in range(10, 190, 10):
            output_file_path = f"{output_folder_path}/QPF_REC_{j}.asc"
            k = int(j / 10 - 1)
            qpf_np = prediction[k, 7:632, 9:534]
            self.save_as_ascii_grid(qpf_np, output_file_path)

    def load_model(self, path: str):
        model = tf.keras.models.load_model(
            path,
            custom_objects={
                "CSI_custom": self.CSI_custom,
                "mae_custom": self.mae_custom,
            },
        )
        return model

    def prediction(self, input_data: np.ndarray):
        pred = self.model.predict(input_data)
        pred = np.squeeze(pred)
        nwcst = np.transpose(pred, (2, 0, 1))
        return nwcst * 255


class RainVer1TfliteModel(RainModel):
    def __init__(self, path: str):
        self.model = self.load_model(path)

    def save_prediction_files(self, input_data: np.ndarray, output_folder_path: str):
        self.create_folder_recursive(output_folder_path)
        prediction = self.prediction(input_data)
        for j in range(10, 190, 10):
            output_file_path = f"{output_folder_path}/QPF_REC_tflite_{j}.asc"
            k = int(j / 10 - 1)
            qpf_np = prediction[k, 7:632, 9:534]
            self.save_as_ascii_grid(qpf_np, output_file_path)

    def load_model(self, path: str):
        model = Interpreter(model_path=path)
        model.allocate_tensors()
        return model

    def prediction(self, input_data: np.ndarray):
        # 입력 데이터 변환 및 설정
        feature = np.array(input_data / 255.0, dtype=np.float32)
        input_details = self.model.get_input_details()
        output_details = self.model.get_output_details()
        self.model.set_tensor(input_details[0]["index"], feature)

        # 모델 실행
        self.model.invoke()

        # 출력 데이터 가져오기
        pred = self.model.get_tensor(output_details[0]["index"])
        pred = np.squeeze(pred)
        nwcst = np.transpose(pred, (2, 0, 1))
        return nwcst


class RainVer2Model(RainModel):
    def __init__(self, path: str):
        """
        RainVer2Model 클래스의 생성자입니다.

        path:
          모델 파일이 들어있는 폴더의 경로이며, "model-best_fcst_{j}min.tflite" 형식을 따라야 합니다.
          j에는 10의 배수인 정수가 180까지 들어갑니다.
        """
        self.model: list[Interpreter] = self.load_model(path)

    def save_prediction_files(self, input_data: np.ndarray, output_folder_path: str):
        self.create_folder_recursive(output_folder_path)
        prediction = self.prediction(input_data)
        for j in range(10, 190, 10):
            output_file_path = f"{output_folder_path}/QPF_{j}.asc"
            k = int(j / 10 - 1)
            self.save_as_ascii_grid(prediction[k], output_file_path)

    def load_model(self, path: str):
        return self.__zip_model(path)

    def __zip_model(self, path: str):
        models = []
        for i in range(10, 190, 10):
            pre_model = f"{path}/model-best_fcst_{i}min.tflite"
            model = Interpreter(model_path=pre_model)
            model.allocate_tensors()
            models.append(model)
        return models

    def prediction(self, input_data: np.ndarray):
        feature = np.array(input_data / 255.0, dtype=np.float32)
        nwcsts = []
        for model in self.model:
            input_details = model.get_input_details()
            output_details = model.get_output_details()
            model.set_tensor(input_details[0]["index"], feature)
            model.invoke()
            nwcst = model.get_tensor(output_details[0]["index"])
            nwcst = self.data_postprocessing(nwcst) * 255.0
            nwcsts.append(nwcst)
        return nwcsts
