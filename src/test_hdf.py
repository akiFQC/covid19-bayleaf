import numpy as np
import h5py
from matplotlib import pyplot as plt
import pandas as pd

<<<<<<< HEAD
with h5py.File("../data/test_data/MCD15A2H.A2020137.h27v06.006.2020148021544.hdf",'r') as f:
=======
with h5py.HDF("../data/test_data/MCD15A2H.A2020137.h27v06.006.2020148021544.hdf",'r') as f:
>>>>>>> master
    print(f.keys())    
    lst=f['Image_data/LAI_AVE']

    desc=lst.attrs['Data_description']
    errdn=lst.attrs['Error_DN']
    maxdn=lst.attrs['Maximum_valid_DN']
    mindn=lst.attrs['Minimum_valid_DN']
    slope=lst.attrs['Slope']
    offset=lst.attrs['Offset']
    unit=lst.attrs['Unit']
    ar = np.array(lst)
    valid = np.where( ar==errdn , -1, ar )
    value = valid*slope + offset
    print(value)
