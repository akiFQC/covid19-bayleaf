from pprint import pprint
import os
import glob
from matplotlib import pyplot as plt
import numpy as np
from pyhdf.SD import SD, SDC  # HDF library module
import datetime
import pandas as pd



def load(dirpath="../input_data", tile="h27v07"):
    qpath  =  os.path.join(dirpath, "*."+tile+".006*.hdf")
    pathes = list(set(glob.glob(qpath)))
    print(pathes)
    file = SD(pathes[0])
    datasets_dic = file.datasets()
    keys = list(datasets_dic.keys())
    df = pd.DataFrame(columns= ["date"]+ keys)

    for pa in pathes:
        file = SD(pa)
        datestr = pa.split(".")[-5]
        datestr = datestr[1:]
        date = datetime.datetime.strptime(datestr, "%Y%d%m")
        di = {"date":date}
        for k in keys:
            x = np.array(file.select(k)[:,:])
            di[k] = x
    
        df=df.append(di, ignore_index=True)
    return df

def main():
    df = load()

    print(df)
    print(df["Lai_500m"], type(df["Lai_500m"]))
    plt.imshow(df["Lai_500m"].iloc[0])
    plt.show()

if __name__=="__main__":
    main()
