import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# min of the matrix
print(f'min of the matrix is: {np.min(a)}')

# max of the matrix along axis 1 (rows)
print(f'max of the matrix along axis 1 is: {np.max(a, axis=1)}')

# sum of the matrix along axis 1 (rows)
print(f'sum of the matrix along axis 1 is: {np.sum(a, axis=1)}')

# Reorganizing array to 4x2
reshaped_a = np.reshape(a, (4, 2))
print(f'Reorganizing the array a from 2x4 to 4x2:\n{reshaped_a}')

# Vertical stack
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(f'After the vertical stacking: \n {np.vstack([v1, v2])}')

# Horizontal stack
horizontal_stack = np.hstack([v1, v2])
print(f'Array after horizontal stacking: \n {horizontal_stack}')
