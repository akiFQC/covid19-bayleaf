from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
from pyhdf.SD import SD, SDC  # HDF library module

file = SD(
    "./input_data/MCD15A3H.A2019209.h26v06.006.2019214040331.hdf", SDC.READ
)  # SD=scientific data
print(file.info())  # show details of the SD
datasets_dic = file.datasets()

for idx, sds in enumerate(datasets_dic.keys()):
    print(idx, sds)

sds_obj = file.select("FparLai_QC")
image = sds_obj.get()
print(image.shape)
plt.imshow(image)
plt.show()
pprint(sds_obj.attributes())
