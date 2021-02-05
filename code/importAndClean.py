import numpy as np
import pandas as pd
import datetime
import csv
import os
import nbimporter
import torch
from torch import nn

#path to curr directory

#read data from scripps buoys for each year
tp_offshore_data = [readData(dir_path + "/data/46225h201{}.txt".format(x)) for x in range(3, 10)]
#scripps_offshore_data = [readData(dir_path + "/data/46254h201{}.txt".format(x)) for x in range(5, 10)]
scripps_nearshore_data = [readData(dir_path + "/data/ljpc1h201{}.txt".format(x)) for x in range(3, 10)]


tp_offshore_cleaned = pd.concat([cleanColumnsFeatures(x) for x in tp_offshore_data], axis = 0, ignore_index=True)
scripps_nearshore_cleaned = pd.concat([cleanColumnsLabels(x) for x in scripps_nearshore_data], axis = 0, ignore_index=True)
                            
tp_offshore_cleaned = min_max_normalize(tp_offshore_cleaned, "MWD")

matched_label_data = matchDataByTime2(tp_offshore_cleaned, scripps_nearshore_cleaned)
