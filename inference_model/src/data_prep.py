import numpy as np


def create_sequences(data, leng):
    xs, ys = [], []
    for i in range(len(data)-leng):
        x = data.iloc[i:(i+leng)]
        y = data.iloc[i+leng]
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)