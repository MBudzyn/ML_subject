import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os, sys

data_directory = "netflix_titles.csv"
print(os.path.isfile(data_directory))
data = pd.read_csv(data_directory, low_memory=False, index_col=0)


class NetflixData:
    def __init__(self, data):
        self.data = data


