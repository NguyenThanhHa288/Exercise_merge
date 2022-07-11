import glob
import json

import pandas as pd

file_humidity = ["E:/TaiLieu_PhanMem2/Python/merge_data/data/jwa_rawdata/jwa_rawdata/humidity/2022/01/*",
                 "E:/TaiLieu_PhanMem2/Python/merge_data/data/jwa_rawdata/jwa_rawdata/humidity/2022/02/*",
                 "E:/TaiLieu_PhanMem2/Python/merge_data/data/jwa_rawdata/jwa_rawdata/humidity/2022/03/*",
                 "E:/TaiLieu_PhanMem2/Python/merge_data/data/jwa_rawdata/jwa_rawdata/humidity/2022/04/*"]


def merge():
    global file_28
    total = []
    for month_file in file_humidity:
        all_date_file = glob.glob(month_file)
        for date_file in all_date_file:
            all_files = glob.glob(date_file)
            for link in all_files:
                link = link.replace("\\", "/") + '/*'
                all_json = glob.glob(link)
                for jsons in all_json:
                    jsons = jsons.replace("\\", "/")
                    f = open(jsons)
                    data = json.load(f)
                    data_train = data["product"][0]["point"]
                    data_train1 = data_train[0]["forecast"]
                    for count in range(len(data_train1)):
                        object = data_train1[count]
                        print(object["time"], object["Precip"][0], object["humidity"][0])
                        total.append({
                            "forecast_time": object["time"],
                            "Precip": object["Precip"][0],
                            "humidity": object["humidity"][0]
                        })
    file_28 = pd.DataFrame(total)
    return file_28


file_28 = merge()
file_28.to_csv("E:/TaiLieu_PhanMem2/Python/merge_data/data_csv/data_feature/data_humitity/humidity_01.csv", index=False)
