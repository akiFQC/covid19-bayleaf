from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD, SDC  # HDF library module
import os
import cv2
from src.data_loader import load


def conver_to_numpy(hdf_file_path):
    file = SD(hdf_file_path, SDC.READ)  # SD=scientific data
    # datasets_dic = file.datasets()
    sds_obj = file.select("FparLai_QC")
    image = sds_obj.get()
    return image


if __name__ == "__main__":
    IMG_SIZE = 256  # 画像サイズ
    BLOCK_SIZE = 64  # 黒ブロックサイズ

    # 動画作成
    fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
    video = cv2.VideoWriter("ImgVideo.mp4", fourcc, 20.0, (IMG_SIZE, IMG_SIZE))

    hdf_image_files = os.listdir("./input_data/data_h27v07")

    for img_file in hdf_image_files:
        # img = cv2.imread(img_file)
        image = conver_to_numpy(img_file)
        video.write(img)

    video.release()
