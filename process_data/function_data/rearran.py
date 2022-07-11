from datetime import timedelta

import pandas as pd

data = pd.read_csv(
    'E:/TaiLieu_PhanMem2/Python/merge_data/data_csv/data_feature/weather/weather_01.csv')

data["forecast_time"] = pd.to_datetime(data["forecast_time"]).dt.tz_localize(None) + timedelta(hours=9)
data = data.sort_values(by='forecast_time', ascending=True)

data_02 = data.drop_duplicates(subset=['forecast_time', 'device_id'], keep='first')

data_02.to_csv('E:/TaiLieu_PhanMem2/Python/merge_data/data_csv/data_feature/weather/weather_02.csv',
               index=False)
