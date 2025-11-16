import numpy as np

a = np.arange(15).reshape(3,5)

# Print out the attributes of a
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize);
print(a.size)
print(type(a))

b = np.array([6, 7, 8])

# Print out b, along with its type
print(b)
print(type(b))