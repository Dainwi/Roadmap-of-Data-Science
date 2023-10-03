import numpy as np

# Define matrices a and b
a = np.array([[4, 8, 6]])
b = np.array([[6, 0], [7, 4], [3, 3]])

# Multiply the matrices
# The number of columns in matrix a must match the number of rows
# in matrix b for matrix multiplication to be defined.
result = np.matmul(a, b)

# Print the result of matrix multiplication
print(f'After multiplying the matrices:\n{result}')

# Find the determinant of matrix a
# a = np.array([[4, 8, 6]]) is not an identity matrix
a = np.identity(3, dtype='int16')
determinant_a = np.linalg.det(a)
print(determinant_a)
print(f'Determinant of matrix a is: {determinant_a}')
