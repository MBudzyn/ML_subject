import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, sys


data_directory = "netflix_titles.csv"




def ignore_first_space(obj):
    return str(obj).lstrip(" ")
def cut_to_first_space(obj):
    return str(obj).split(" ")[0]


class NetflixData:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data = self.load_data()

    def load_data(self):
        return pd.read_csv(self.data_dir, low_memory=False, index_col=2)

    def print_data_info(self):
        print(self.data.info())
        print(self.data.head())

    def parse_type_to_int(self):
        self.data['type'] = self.data['type'].map({'TV Show': 0, 'Movie': 1})

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

    def view_duration(self):
        print(self.data["movie duration"].unique())
        print(self.data['tv show duration'].unique())
        print(self.data['movie duration'].describe())
        print(self.data['tv show duration'].describe())

    def view_rating(self):
        print(self.data['rating'].unique())
        print(self.data['rating'].describe())
        print(self.data['rating'].value_counts())
        print(self.data[self.data['rating'] == "84 min"])

    def fill_empty_rating(self):
        self.data["rating"] = self.data['rating'].fillna("No category")

    def fill_empty_duration(self):
        self.data["duration"] = self.data['duration'].fillna(self.data["rating"])

    def duration_split(self):
        self.data['movie duration'] = self.data['duration'].where(self.data['type'] == True)
        self.data['tv show duration'] = self.data['duration'].where(self.data['type'] == False)

    def duration_to_int(self):
        self.data['movie duration'] = self.data['movie duration'].dropna().apply(cut_to_first_space).astype(float)
        self.data['tv show duration'] = self.data['tv show duration'].dropna().apply(cut_to_first_space).astype(float)



netflix_data = NetflixData(data_directory)
netflix_data.drop_id()
netflix_data.parse_type_to_int()
netflix_data.print_data_info()
print("=================")
netflix_data.empty_values_description()
netflix_data.view_date_added_format()
netflix_data.parse_date_added()
netflix_data.duration_split()
netflix_data.print_data_info()
netflix_data.view_duration()
netflix_data.print_data_info()
#netflix_data.fill_empty_rating()
netflix_data.view_rating()
netflix_data.fill_empty_duration()
netflix_data.duration_split()
netflix_data.duration_to_int()
netflix_data.print_data_info()


