import numpy as np

# 3D array a
a = np.array([[[1, 2, 3], [4, 5, 6]],
              [[7, 8, 9], [0, 0, 0]],
              [[11, 12, 13], [14, 15, 16]]])
# Printing the 3D array
# print(f'This is a 3D array: {a}')

# Get Dimension
print(f'The dimension of the 3d array is: {a.ndim}')

# Get Shape (Output format is (layers, row, column))
print(f'The shape of the 3D array is: {a.shape}')


print('\n')

# 3D array b
b = np.array([[[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]],
              [[10, 11, 12],
               [13, 14, 15],
               [16, 17, 18]],
              [[19, 20, 21],
               [22, 23, 24],
               [25, 26, 27]]])
# Get Dimension
print(f'The dimension of the b is: {b.ndim}')

# Get Shape (Output format is (layers, row, column))
print(f'The shape of the b is: {b.shape}')

# Get specific element (work outside in)
print(f'The specific element from the array b:  {b[1, 0, 2]}')

# Replace the specific element
b[0, 0, 0] = 0
print(f'The specific element from the array b after replacement:  {b[0, 0, 0]}')

