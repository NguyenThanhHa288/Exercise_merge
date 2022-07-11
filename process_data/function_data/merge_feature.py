import pandas as pd

data_1 = pd.read_csv(
    'data_csv/data_taget/concat_file.csv')
data_2 = pd.read_csv(
    'data_csv/data_feature/data_merge_v1/feature_3.csv')

data_test = pd.merge(data_1, data_2, on=["forecast_time", "device_id"], how='outer')
data_test_1 = data_test.drop_duplicates(subset=['forecast_time', 'device_id'], keep='first')
data_test_2 = data_test_1.sort_values(by='forecast_time')

data_test_2.to_csv('data_csv/data_feature/data_merge_v1/result.csv', index=False)
