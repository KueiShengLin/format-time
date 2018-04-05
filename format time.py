"""
This program can convert time old format to new format in csv file or pandas dataframe

dataset = The data which you want to format
time_column_name = The column in dataset you want to convert
old_format = The format in your dataset, if you format is "timestamp" pleases input "timestamp" in this parameter
new_format = The format you want to convert,
             if you want to convert to timestamp pleases input "timestamp" in this parameter
csv_name = Output csv file name
csv_save = If you want to output the file please change this parameter to "True", default is "False"

The time directives are in https://docs.python.org/2/library/time.html
"""

import time
import pandas as pd


def format_time(dataset=None, time_column_name="day", old_format="%Y/%m/%d %H:%M", new_format="%Y-%m-%d %H:%M:%S",
                csv_name="time_format.csv", csv_save=False):

    if isinstance(dataset, pd.DataFrame) is False:
        dataset = pd.read_csv(dataset)

    if old_format == "timestamp":
        time_format = [time.gmtime(t) for t in dataset[time_column_name]]
    else:
        time_format = [time.strptime(t,  old_format) for t in dataset[time_column_name]]

    if new_format == "timestamp":
        time_format = [time.mktime(i) for i in time_format]
    else:
        time_format = [time.strftime(new_format, i) for i in time_format]

    dataset[time_column_name] = time_format

    if csv_save is True:
        if csv_name[-4] != ".":
            csv_name += ".csv"

        elif csv_name[-3:] != "csv":
            print("I can't save to", csv_name[-3:], " :(")
            return dataset

        dataset.to_csv(csv_name, index=False)

    return dataset
#
