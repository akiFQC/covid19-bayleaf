import datetime
import os
from pathlib import Path
from pprint import pprint

import cv2
import matplotlib.pyplot as plt

# from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import numpy as np
import pandas as pd
from pyhdf.SD import SD, SDC  # HDF library module
from cv2 import VideoWriter, VideoWriter_fourcc
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


def convert_to_numpy(hdf_file_path):
    file = SD(hdf_file_path, SDC.READ)  # SD=scientific data
    # datasets_dic = file.datasets()
    sds_obj = file.select("FparLai_QC")
    image = sds_obj.get()
    return image


def animate(i):
    image = convert_to_numpy(image_path[i])
    return plt.imshow(image)


if __name__ == "__main__":
    fig = plt.figure()
    width = 1280
    height = 720
    FPS = 24
    seconds = 10
    IMG_SIZE = 256  # 画像サイズ
    input_data_dir = Path("./input_data/data_h27v07")
    df = load_into_dataframe(input_data_dir)
    df = df.sort_values("date").reset_index(drop=True)
    # print(df)
    images = []
    for image_path in df.path:
        image = convert_to_numpy(str(image_path))
        image = cv2.resize(image, (255, 255))
        image = plt.imshow(image, animated=True)
        images.append([image])
    ani = animation.ArtistAnimation(
        fig, images, interval=50, blit=True, repeat_delay=1000
    )
    # ani.save("dynamic_images.mp4")

    plt.show()
