import torch
import numpy as np
from torchvision import datasets


# a WaveDataset class
# inputs: file_lst - a list of cleaned and matched files in the form of pandas dataframes
# , the last of which contains the desired label data in a 1D array (most likely Significant Wave Height)
# replace junk values with NaN

class WaveDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.len = data.shape[0]
        self.data = data

    def __getitem__(self, index):
        # ABSTRACTION, LEARN ABOUT NUMPY SHAPE
        features = torch.tensor(self.data.loc[index, ["WVHT_x", "DPD", "APD", "MWD"]], requires_grad=True).float()
        label = torch.tensor(self.data.loc[index, "WVHT_y"], requires_grad=True).float()
        return features, label  # ABSTRACTION, LEARN ABOUT NUMPY SHAPE

    def __len__(self):
        return self.len


