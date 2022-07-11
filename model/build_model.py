import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

from model.function_model import miss_value, normalize, add_bias

data = pd.read_csv('E:/TaiLieu_PhanMem2/Python/merge_data/data_csv/data_feature/data_merge_v1/result_end.csv')

m = len(data["value"])

solar_pv = np.array((data["solar_pv"]))
solar_radiation = np.array((data["solar_radiation"]))
temperature = np.array((data["temperature"]))
humidity = np.array((data["humidity"]))
X = np.array([solar_pv, solar_radiation, temperature, humidity]).T

y = np.array(data["value"]).reshape((m, 1))

X = miss_value(X)
X = add_bias(X)
y = miss_value(y)

(X_train_val, X_test, y_train_val, y_test) = train_test_split(X, y, test_size=0.2)
(X_train, X_val, y_train, y_val) = train_test_split(X_train_val, y_train_val, test_size=0.2)

X_train = normalize(X_train)
X_test = normalize(X_test)

# y_train = normalize(y_train)
# y_test = normalize(y_test)

model = Sequential()
model.add(Dense(64, input_shape=(X_train.shape[1],), activation='relu'))
model.add(Dense(32, input_dim=16, activation='relu'))
model.add(Dense(16, input_dim=8, activation='relu'))
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(1, activation='relu'))
model.summary()

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae', 'categorical_accuracy'])

model.fit(X_train, y_train, epochs=100, batch_size=8, validation_data=(X_val, y_val))

loss, mae, acc = model.evaluate(X_test, y_test)
model.save("my_model.h5")

print("Loss = ", loss)
print("Acc = ", acc)

y_predict1 = model.predict(X_test)

print(y_predict1, y_test)
