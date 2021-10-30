import pandas as pd
import numpy as np
import operator
import dataset
import csv
import os

def load_dataset(input_csv):
    df = pd.read_csv(input_csv, header=0, low_memory=False)
    return df

def dataframe_to_csv(pd_df, filename):
    pd_df.to_csv(filename, index=False, quoting=csv.QUOTE_NONNUMERIC)
    return

def data_to_file_two_values(data, headings, filename):
    with open(filename, mode='w') as file_writer:
        file_writer.write(headings + "\n")
        for row in data:
            file_writer.write(str(row[0]) + ',"' + str(row[1]) + '"' + "\n")
    return

def path_checker(path):
    path = path.split("/")
    path_so_far = ""
    for dir in path:
        path_so_far += "/" + dir
        if os.path.exists(path_so_far) == False:
            path_creator(path_so_far)
    return

def path_creator(path):
    os.mkdir(path)
    return

def path_fetcher(path):
    return os.listdir(path)

def sort_dict(dictionary):
    return dict(sorted(dictionary.items(),
                    key=operator.itemgetter(1),
                    reverse=True))


def print_df_headings(file):
    df = load_dataset(file)
    for heading in file.head():
        print(heading)
