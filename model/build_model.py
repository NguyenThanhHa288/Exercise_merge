import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import Dense

from model.function_model import miss_value, add_bias


def process_data(get_data):
    m = len(get_data["value"])
    X = np.array(get_data[["solar_pv", "solar_radiation", "temperature", "humidity"]].values)
    y = np.array(get_data["value"].values).reshape((m, 1))

    X = miss_value(miss_value(X))
    y = miss_value(y)

    X = add_bias(X)
    # X = normalize(X)
    # y = normalize(y)

    return X, y


data = pd.read_csv('E:/TaiLieu_PhanMem2/Python/merge_data/data_csv/data_feature/data_merge_v1/result_end.csv')

filt_train = (data["forecast_time"] < "2022-03-18 00:00:00")
data_train = data.loc[filt_train]

filt_val = (data["forecast_time"] >= "2022-03-18 00:00:00")
data_val = data.loc[filt_val]
filt_val = (data_val["forecast_time"] < "2022-04-01 12:00:00")
data_val_1 = data_val.loc[filt_val]

X_train, y_train = process_data(data_train)
X_val, y_val = process_data(data_val)

model = Sequential()
model.add(Dense(64, input_shape=(X_train.shape[1],), activation='relu'))
model.add(Dense(32, input_dim=16, activation='relu'))
model.add(Dense(16, input_dim=8, activation='relu'))
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(1, activation='relu'))
model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=100, batch_size=8, validation_data=(X_val, y_val))

model.save("my_model.h5")
