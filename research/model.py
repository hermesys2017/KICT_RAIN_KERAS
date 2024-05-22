import keras.backend as K
import numpy as np
import tensorflow as tf
from tensorflow.lite.python import interpreter as interpreter_wrapper


def ver1_save_prediction_files(input_data, folder_path):
    model = __load_ver1_model("path")  # 여기 모델 path를 정해주기
    prediction = __prediction_rec(model, input_data)
    __save_asc(prediction, folder_path)


def ver2_save_prediction_files(input_data, folder_path):
    pass


def __load_ver1_model(path):
    model = tf.keras.models.load_model(
        path,
        custom_objects={"CSI_custom": __CSI_custom, "mae_custom": __mae_custom},
    )
    return model


def __load_ver2_model(path):
    interpreter = interpreter_wrapper.Interpreter(model_path=path)
    interpreter.allocate_tensors()
    return interpreter


def __get_tensor(interpreter: interpreter_wrapper.Interpreter):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    return input_details, output_details


def __ver2_prediction_rec(interpreter: interpreter_wrapper.Interpreter):
    feature = np.array(feature / 255.0, dtype=np.float32)  # FLOAT64에서 FLOAT32로 변환
    input_details, output_details = __get_tensor(interpreter)
    interpreter.set_tensor(input_details[0]["index"], feature)
    # 모델 실행
    interpreter.invoke()

    # 출력 데이터 가져오기
    nwcst = interpreter.get_tensor(output_details[0]["index"])
    nwcst = __data_postprocessing(nwcst) * 255.0
    return nwcst


def __prediction_rec(model_instance, input_data):  # 예측시 recursive 안함
    input_data = __data_preprocessing(input_data)
    pred = model_instance.predict(input_data)
    pred = np.squeeze(pred)
    nwcst = np.transpose(pred, (2, 0, 1))
    return nwcst * 255


def __save_asc(nwcst, path):
    for j in range(10, 190, 10):
        output_file_path = path + "/" + str(j) + ".asc"
        k = int(j / 10 - 1)
        qpf_np = nwcst[k, 7:632, 9:534]
        __save_as_ascii_grid(qpf_np, output_file_path)


# f1 score 계산
def __Rain(array):
    R = array * 255.0
    return R


def __CSI_m(y_true, y_pred):
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


def __CSI_custom(y_true, y_pred):
    score = tf.py_function(
        func=__CSI_m, inp=[y_true, y_pred], Tout=tf.float32, name="CSI_custom"
    )
    return score


def __mae_custom(y_true, y_pred):
    y_pred = tf.convert_to_tensor(y_pred)
    y_true = tf.convert_to_tensor(y_true)
    y_true = __Rain(y_true)
    y_pred = __Rain(y_pred)
    thr1 = K.greater(y_true, 0.1)
    loss1 = K.mean(K.abs(y_true[thr1] - y_pred[thr1]))
    arr = [loss1]
    value_not_nan = tf.dtypes.cast(
        tf.math.logical_not(tf.math.is_nan(arr)), dtype=tf.float32
    )
    loss0 = tf.math.multiply_no_nan(arr, value_not_nan)
    loss = tf.convert_to_tensor(K.sum(loss0))
    return loss


def __data_preprocessing(X):
    # 0. Right shape for batch
    X = X[np.newaxis, ::, ::, ::]
    return X


def __save_as_ascii_grid(data, output_file):
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

    np.savetxt(output_file, data, fmt="%.2f", header=header, comments="", delimiter=" ")


def __data_postprocessing(nwcst):
    # 0. Squeeze empty dimensions
    nwcst = np.squeeze(np.array(nwcst))
    nwcst = nwcst
    nwcst = np.where(nwcst > 0, nwcst, 0)
    nwcst = nwcst[7:632, 9:534]
    return nwcst
