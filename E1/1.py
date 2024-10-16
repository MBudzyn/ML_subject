import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, sys

data_directory = "netflix_titles.csv"


def ignore_first_space(obj):
    return str(obj).lstrip(" ")

class NetflixData:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data = self.load_data()

    def load_data(self):
        return pd.read_csv(self.data_dir, low_memory=False, index_col=2)

    def print_data_info(self):
        print(self.data.info())
        print(self.data.head())

    def parse_type_to_bool(self):
        self.data['type'] = self.data['type'].map({'TV Show': False, 'Movie': True})

    def parse_date_added(self):
        self.data['date_added'] = self.data['date_added'].apply(ignore_first_space)
        self.data['date_added'] = pd.to_datetime(self.data['date_added'], format="%B %d, %Y")

    def fill_empty_date_added(self):
        self.data['date_added'].fillna(self.data['date_added'].mode()[0], inplace=True)

    def view_date_added_format(self):
        for data in self.data['date_added'].values:
            if len(str(data).split(" ")) > 3:
                print(str(data).split(" "), "length: ", len(str(data).split(" ")))




    def empty_values_description(self):
        print("empty values in data")
        print(self.data.isnull().sum())
        print(f"sum of empty values in the data: {self.data.isnull().sum().sum()}")

    def drop_id(self):
        self.data.drop('show_id', axis=1, inplace=True)



netflix_data = NetflixData(data_directory)
netflix_data.drop_id()
netflix_data.parse_type_to_bool()
netflix_data.print_data_info()
print("=================")
netflix_data.empty_values_description()
netflix_data.view_date_added_format()
netflix_data.parse_date_added()
netflix_data.print_data_info()



