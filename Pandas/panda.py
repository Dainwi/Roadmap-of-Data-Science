import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])
# print(type(s))

# converting the dictionary into a data frame
d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12]}
data_frame = pd.DataFrame(d)
# Printing the data frame
print(f'\nPrinting the data frame \n {data_frame}')

# export the data in csv file
data_frame.to_csv('data.csv', index_label='s no.')

# print(data_frame.head())
print(f'\nReading the csv file \n {pd.read_csv("data.csv")}')

# Get rows and columns of the dataframe
rc = data_frame.shape
print(f'\nGet the number of rows and columns of the dataframe \n {rc}')


# Get the index of the dataframe
index = data_frame.index
print(f'\nGet the index of the dataframe \n {index}')

# Get the columns of the dataframe
columns = data_frame.columns
print(f'\nGet the columns of the dataframe \n {columns}')

# Get the values of the dataframe
values = data_frame.values
print(f'\nGet the values of the dataframe \n {values}')


# Get the datatype of the dataframe
datatype = data_frame.dtypes
print(f'\nGet the datatype of the dataframe \n {datatype}')


# Get the info of the dataframe
info = data_frame.info()
print(f'Get the info of the dataframe \n {info}')

# Get the describe of the dataframe
describe = data_frame.describe()
print(f'\nGet the describe of the dataframe \n {describe}')

# Get the unique values of the dataframe
unique = data_frame.nunique()
print(f'\nGet the unique values of the dataframe \n {unique}')

# Chnage the valuse of specific column on specific index
data_frame.at[1, 'a'] = 100
print(data_frame)
