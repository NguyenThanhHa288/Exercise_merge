import pandas as pd
from keras.saving.save import load_model

from model.build_model import process_data

data = pd.read_csv('E:/TaiLieu_PhanMem2/Python/merge_data/data_csv/data_feature/data_merge_v1/result_end.csv')

filt_test = (data["forecast_time"] >= "2022-04-01 12:00:00")
data_test = data.loc[filt_test]

X_test, y_test = process_data(data_test)

model = load_model("E:/TaiLieu_PhanMem2/Python/merge_data/model/my_model.h5")

y_predict = model.predict(X_test)
print(y_predict)
