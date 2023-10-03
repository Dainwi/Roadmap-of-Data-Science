import numpy as np

a = np.array([1, 2, 3], dtype='int8')
b = np.array([[1.1, 2.0, 3.0], [4.0, 5.0, 6.0]], dtype='float64')

# Print matrix
print(b)

# Get Dimension
print("Dimension", a.ndim)

# Get Type/Size
print('Type: ', b.dtype)
print('Size: ', b.itemsize)
