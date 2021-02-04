import numpy as np
import pandas as pd
import datetime
import csv
import os
import nbimporter
import torch
from torch import nn

#path to curr directory
dir_path = os.path.dirname(os.path.abspath("import_and_clean.ipynb"))

#mutates the data_f to replace float time info to datetime object format
def createDatetimeColumn(data_f):
    datetime_col = []
    num_rows = len(data_f.index)
    for i in range(0, num_rows):
        datetime_col += [datetime.datetime(int(data_f["#YY"][i]), int(data_f["MM"][i]), int(data_f["DD"][i]), int(data_f["hh"][i]), int(data_f["mm"][i]))]
    datetime_col = pd.DataFrame(datetime_col, columns = ['datetime'])
    data_f = data_f.drop(["#YY", "MM", "DD", "hh", "mm"], 1)
    data_f = pd.concat([data_f, datetime_col], axis = 1)
    return data_f

#reads the raw NoAA data int
def readData(filePath):
    #read file
    data_f = pd.read_csv(filepath_or_buffer = filePath, header = 0, skiprows = [1], dtype = 'float', delim_whitespace=True)
    return data_f

#delete undesirable columns from the NoAA data for features and make datetime object
def cleanColumnsFeatures(data_f):
    cleaned_data_f = data_f[["#YY", "MM", "DD", "hh", "mm", "WVHT", "DPD", "APD", "MWD"]]
    cleaned_data_f = createDatetimeColumn(cleaned_data_f)
    return cleaned_data_f

#delete undesirable columns from the NoAA data for features and make datetime object
def cleanColumnsLabels(data_f):
    cleaned_data_f = data_f[["#YY", "MM", "DD", "hh", "mm", "WVHT"]]
    cleaned_data_f = createDatetimeColumn(cleaned_data_f)
    return cleaned_data_f
