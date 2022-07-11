import numpy as np
import pandas as pd
from keras.saving.save import load_model
from sklearn.model_selection import train_test_split

from model.function_model import miss_value, add_bias, normalize


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

X_test = normalize(X_test)

model = load_model("E:/TaiLieu_PhanMem2/Python/merge_data/model/my_model.h5")

y_predict = model.predict(X_test)
print(y_predict)