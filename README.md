# format-time-in-python 3.6
It is annoying that the time format is different in two data, so I make this to convert format

# Parameter
+ dataset = The data which you want to format

+ time_column_name = The column in dataset you want to convert

+ old_format = The format in your dataset, if you format is "timestamp" pleases input "timestamp" in this parameter

+ new_format = The format you want to convert,
             if you want to convert to timestamp pleases input "timestamp" in this parameter

+ csv_name = Output csv file name

+ csv_save = If you want to output the file please change this parameter to "True", default is "False"

The time directives are in: https://docs.python.org/2/library/time.html