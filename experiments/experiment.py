import datetime
import os
from pathlib import Path
from pprint import pprint

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pyhdf.SD import SD, SDC  # HDF library module

from src.data_loader import load


def load_into_dataframe(input_data_dir):
    df = pd.DataFrame(columns=["date"])
    for image_path in input_data_dir.iterdir():
        datestr = image_path.name.split(".")[-5]
        datestr = datestr[1:]
        date = datetime.datetime.strptime(datestr, "%Y%j")
        out_dict = {"date": date, "path": image_path}
        df = df.append(out_dict, ignore_index=True)
    return df


def get_path_df(hdf_file_path):
    file = SD(hdf_file_path, SDC.READ)  # SD=scientific data
    # datasets_dic = file.datasets()
    sds_obj = file.select("FparLai_QC")
    image = sds_obj.get()
    return image


if __name__ == "__main__":
    IMG_SIZE = 256  # 画像サイズ
    input_data_dir = Path("./input_data/data_h27v07")
    df = get_path_df(input_data_dir)
    df = df.sort_values("date").reset_index(drop=True)
    print(df)

    # df = load(str(input_data_dir))
    # print(df)

    # # # 動画作成
    # fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    # video = cv2.VideoWriter("ImgVideo.mp4", fourcc, 20.0, (IMG_SIZE, IMG_SIZE))

    # for img_file in input_data_dir.iterdir():
    #     # img = cv2.imread(img_file)
    #     image = conver_to_numpy(str(img_file))
    #     video.write(image)

    # video.release()
