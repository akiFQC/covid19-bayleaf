import numpy as np
import matplotlib as plt

from . import data_loader


def main():
    df = data_loader.load("../input_data/**")

    print(df.dtypes)

    plt.plot(x=df.date, y=np.mean(df["Lai_500m"]), lw=0, marker=".")



if __name__ == '__main__':
    main()
        
