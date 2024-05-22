import numpy as np


def dataset(files):
    """
    files:
        4개의 파일을 가지고 있어야 함. 각 파일은 30분전, 20분전, 10분전, 현재의 QPE 데이터를 가지고 있어야 함.
    """
    qpe = __qpe_data(files)
    dataset = np.transpose(qpe, (1, 2, 0))
    dataset = np.pad(
        dataset, [(7, 8), (9, 10), (0, 0)], mode="constant", constant_values=0
    )
    feature0 = dataset[:, :, :]
    feature = np.where(feature0 < 0.0, 0, feature0)
    feature = __data_preprocessing(feature)
    return feature


def __read_asc_file(filename):
    data = np.zeros([625, 525], np.float32)  # ASCII랑배열 반대
    data = np.loadtxt(filename, skiprows=6)
    data[data < 0] = 0.0
    return data


def __qpe_data(files):
    input_scans = np.array([__read_asc_file(file) for file in files])
    qpe_scans = np.concatenate([input_scans], axis=0)
    return qpe_scans


def __data_preprocessing(X):
    # 0. Right shape for batch
    X = X[np.newaxis, ::, ::, ::]
    return X
