import numpy as np
import matplotlib as plt

import data_loader


def main():
    df = data_loader.load("../input_data/**")

    print(df.dtypes)
    means = []
    df["mean_lai"] = df["Lai_500m"].apply(lambda x : np.mean(x))

    df.sort_values("date", ascending=True).plot(x="date", y="means_lai",  lw=0, er=".")



if __name__ == '__main__':
    main()
        
