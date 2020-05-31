import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import data_loader
import sklearn
# area = 0:1000  1000:1700 




def main():
    df = data_loader.make_df("../input_data/data_h27v07")
    bin = 10
    rang = np.arange(0, (1000//bin-1)*(700//bin-1))
    col_areas = []
    for i in rang:
        df[f"mean_lai_{i}"]=0
        col_areas.append(f"mean_lai_{i}")
    #print(df)
    for idx in df.index:
        val = data_loader.load(df.loc[idx, "path"])["Lai_500m"]
        for i in rang:
            j = i // (1000//bin)
            k = i % (700//bin)
            
            df.loc[idx, f"mean_lai_{i}"] = np.mean(val[j*bin:(j+1)*bin, k*bin:(k+1)*bin])
        #print(df.loc[idx, :])
    print(df.shape)
#    df.sort_values("date", ascending=True).plot(x="date", y="mean_lai")
 #   plt.show()
    df.to_csv("../input_data/area_lai_5km_mean.csv")


if __name__ == '__main__':
    main()
        
