import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import data_loader


def main():
    df = data_loader.make_df("../input_data/data_h27v07")

    

    df["mean_lai"] = df.path.map(lambda x : np.mean(data_loader.load(x)["Lai_500m"] ))

    df.sort_values("date", ascending=True).plot(x="date", y="mean_lai")
    plt.show()


if __name__ == '__main__':
    main()
        
