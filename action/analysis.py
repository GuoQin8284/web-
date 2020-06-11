import json
import os

from config import BASE_DIR


def analysis_data(file_name):
    file_path = BASE_DIR+os.sep+"data"+os.sep+file_name
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        json_list = json.load(f)
        data_list = list()
        for i in json_list:
            a = (i,)
            data_list.append(a)
        return data_list
