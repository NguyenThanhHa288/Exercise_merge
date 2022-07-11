import glob
import json

import pandas as pd

file_humidity = ["E:/TaiLieu_PhanMem2/Python/merge_data/data/jwa_rawdata/jwa_rawdata/solar_radiation/2022/01/*",
                 "E:/TaiLieu_PhanMem2/Python/merge_data/data/jwa_rawdata/jwa_rawdata/solar_radiation/2022/02/*",
                 "E:/TaiLieu_PhanMem2/Python/merge_data/data/jwa_rawdata/jwa_rawdata/solar_radiation/2022/03/*",
                 "E:/TaiLieu_PhanMem2/Python/merge_data/data/jwa_rawdata/jwa_rawdata/solar_radiation/2022/04/*"]


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
                    device_id = jsons[jsons.index('#') + 1:jsons.index('.json')]
                    device_id = device_id[device_id.index('#') + 1:]
                    f = open(jsons)
                    data = json.load(f)
                    data_train = data["results"][0]["values"]
                    for count in range(len(data_train)):
                        object = data_train[count]
                        print(object["forecast_time"], object["solar_radiation"]["value"])
                        total.append({
                            "forecast_time": object["forecast_time"],
                            "device_id": device_id,
                            "solar_radiation": object["solar_radiation"]["value"]
                        })
    file_28 = pd.DataFrame(total)
    return file_28


file_28 = merge()
file_28.to_csv("E:/TaiLieu_PhanMem2/Python/merge_data/data_csv/data_feature/solar_radiation/solar_radiation_01.csv",
               index=False)
