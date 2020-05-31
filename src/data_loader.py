from pprint import pprint
import os
import glob
from matplotlib import pyplot as plt
import numpy as np
from pyhdf.SD import SD, SDC  # HDF library module
import datetime
import pandas as pd



def make_df(dirpath="../input_data", tile="h27v07"):
    qpath  =  os.path.join(dirpath, "*."+tile+".006*.hdf")
    pathes = list(set(glob.glob(qpath)))
    print(pathes)
    df = pd.DataFrame(columns= ["date", "path"])

    for pa in pathes:
        datestr = pa.split(".")[-5]
        datestr = datestr[1:]
        date = datetime.datetime.strptime(datestr, "%Y%j")
        df=df.append({"date":date, "path":pa}, ignore_index=True)
    return df

def load(path):
    print(path)
    file = SD(path , SDC.READ)
    keys = file.datasets()
    data = file.select(keys)
    dic = {}
    print(data)
    for k,da in zip(keys, data):
        dic[k] = da[:,:]  


def main():
    df = make_df()
    print(df)
    val = load(df["path"].iloc[0])
    plt.show(val["Lai_500m"])

if __name__=="__main__":
    main()
