from data import dataset
from model_oop import RainVer1Model, RainVer2Model


def ver1_main(files):
    input_data = dataset(files)
    model = RainVer1Model("path")  # 여기 모델 path를 정해주기
    model.save_prediction_files(
        input_data, "path"
    )  # 여기 저장할 folder path를 정해주기


def ver2_main(files):
    input_data = dataset(files)
    model = RainVer2Model("path")  # 여기 모델 path를 정해주기
    model.save_prediction_files(
        input_data, "path"
    )  # 여기 저장할 folder path를 정해주기
