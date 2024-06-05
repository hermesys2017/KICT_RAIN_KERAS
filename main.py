from data import dataset
from model_oop import RainVer1Model, RainVer2Model


def ver1_main(files):
    input_data = dataset(files)
    model = RainVer1Model(
        "./models/model-best_rec_180min_f.h5"
    )  # 여기 모델 path를 정해주기
    model.save_prediction_files(
        input_data, "output/ver1/"
    )  # 여기 저장할 folder path를 정해주기


def ver2_main(files):
    input_data = dataset(files)
    model = RainVer2Model("./models")  # 여기 모델 폴더 path를 정해주기
    model.save_prediction_files(
        input_data, "output/ver2/"
    )  # 여기 저장할 folder path를 정해주기


if __name__ == "__main__":
    files = ["path"]  # 여기 파일 path를 정해주기
    ver1_main(files)
    ver2_main(files)
