import numpy as np

a = np.array([1, 2, 3, 4])

# Printing the element of the array
print(a)

# Printing the array after adding 2 with each element of the array
a = a + 2
print(a)

# Printing the array after subtract 2 with each element of the array
a = a - 2
print(a)

# Printing the array after multiply 2 with each element of the array
a = a * 2
print(a)

# Printing the array after devide 2 with each element of the array
a = a / 2
print(a)

# Add two array
b = np.array([5, 6, 7, 8])
print(f'array A + Array B: {a + b}')

# sin of the element of the array
print(f'sin of the each element of the array a is: {np.sin(a)}')

# cos of the element of the array
print(f'cos of the each element of the array a is: {np.cos(a)}')

