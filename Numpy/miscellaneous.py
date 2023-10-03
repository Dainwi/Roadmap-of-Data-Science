import numpy as np

# Load data from file
# file_data = np.genfromtxt('data.txt', delimiter=',').astype('int16')
file_data = np.genfromtxt('data.txt', delimiter=',', dtype='int16')
print(f'File data is \n {file_data}')

# Boolean Masking and Advance indexing

# Boolean Masking
print(f'is file data is more then 50 \n {file_data > 50}')

# Advance indexing
print(f'data which is more then 50 \n {file_data[file_data > 50]}')
print(f'\n Printing the element from the specific index: {file_data[[0, 1, 2]]}')
