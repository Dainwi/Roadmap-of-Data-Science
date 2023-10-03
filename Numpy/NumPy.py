import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype='int16')
# print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)

# Get dimension
print(a.ndim)

# Get shape (output is in the number of row and column)
print(a.shape)
print(f'The shape of b is: {b.shape}')

# Get Size
print(a.itemsize)

# Get Data Type
print(a.dtype)

# Accessing/Changing specific elements, rows, columns, etc

# Get a specific element [row, col]
print(b[1, 2])

# Get a specific row
print(b[0, :])

# Getting a Little more fancy [startIndex : endIndex : stepSize]
print(b[0, 1:2:2])
#
b[:, 2] = [1, 2]
print(b)


# Initializing different types of array

# All 0s matrix
all_zero_matrix = np.zeros((2, 3))
print('All 0s matrix: ')
print(all_zero_matrix)

print('\n')
# All 1s matrix
print('All 1s matrix: ')
all_ones_matrix = np.ones((2, 3))
print(all_ones_matrix)

print('\n')
# Any other number
other_number_matrix = np.full((2, 3), 99)
print('All other numbers matrix: ')
print(other_number_matrix)

print('\n')
# Random decimal number matrix
random_num_matrix = np.random.rand(4, 2, 3)
print('Random decimal number matrix')
print(random_num_matrix)

print('\n')
# Random integer number matrix
random_int_num_matrix = np.random.randint(0, 9, size=(3, 3))
print('Random integer number matrix')
print(random_int_num_matrix)


print('\n')
# The identity matrix
identity_matrix = np.identity(3, dtype='int8')
print('The Identity matrix')
print(identity_matrix)

print('\n')
# Repeat an array
arr = np.array([[1, 2, 3]])
repeated_array = np.repeat(arr, 3, axis=0)
print('Repeated array is')
print(repeated_array)

# Copying the array
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print(f'The array a has: {a}')
print(f'The array b has: {b}')
