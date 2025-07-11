from kict_rain_forecast.services.data import dataset
from kict_rain_forecast.services.model_oop import (
    RainVer1Model,
    RainVer1TfliteModel,
    RainVer2Model,
)


def ver1_main(files, model_path, output_path):
    input_data = dataset(files)
    model = RainVer1Model(model_path)
    model.save_prediction_files(input_data, output_path)


def ver2_main(files, model_path, output_path):
    input_data = dataset(files)
    model = RainVer2Model(model_path)
    model.save_prediction_files(input_data, output_path)


def ver1_tflite_main(files, model_path, output_path):
    input_data = dataset(files, is_ver1_tflite=True)
    model = RainVer1TfliteModel(model_path)
    model.save_prediction_files(input_data, output_path)
