import numpy as np
from numpy import pi


# Create a basic array datatype with numpy and print out its attributes

print("An example of a basic range. \n\n --------------------------------------\n\n")

a = np.arange(15).reshape(3,5)

# Print out the attributes of a
print("a = ", a, "\n")
print("a.shape = ", a.shape, "\n")
print("a.ndim = " , a.ndim)
print("a.dtype = ", a.dtype.name)
print("a.itemsize = ", a.itemsize);
print("a.size = ", a.size)
print("type(a) = ", type(a), "\n")

print ("An example of a basic array. \n\n -------------------------------------\n\n")
b = np.array([6, 7, 8])

# Print out b, along with its type
print("b = ", b, "\n")
print("type(b) = ", type(b), "\n")


a = np.array([2, 3, 4])

print("New a = " , a, "\n")
print("New a.dtype = ", a.dtype)

b = np.array([1.2, 3.5, 5.1])
print ("New b.dtype = ", b.dtype, "\n")

b = np.array([(1.5,2,3), (4,5,6)])

print("Multidimensional b = ", b, "\n")

c = np.array([[1,2], [3,4]], dtype=complex)

print("c = ", c, "\n")

print(np.zeros((3,4)))

print(np.ones((2,3,4), dtype = np.int16))

print(np.empty((2,3)))

print(np.arange(10,30,5), "\n\n")

print(np.arange(0,2,0.3), "\n\n")

print (np.linspace(0,2,9))

x = np.linspace(0, 2*pi, 100)

f = np.sin(x)

print ("x = ", x, "\n")
print("f = ", f, "\n\n")

print("------------------------------------------------------------\n\n")
print("Basic Array Operations\n\n")
print("------------------------------------------------------------\n\n")

a = np.array([20, 30, 40, 50])
b = np.arange(4)

c = a - b

print(a, "\n - \n", b, "\n = \n", c, "\n\n")
print("b^2 = ", b**2, "\n\n")
print("10 * np.sin(a) = ", 10*np.sin(a), "\n\n")
print("a < 35 = ", a < 35, "\n\n")

A = np.array([[1,1], [0,1]])
B = np.array([[2,0], [3,4]])

print (A, "\n * \n", B, "\n = \n", A*B, "\n\n")
print(A, "\n @ \n", B, "\n = \n", A@B, "\n")
print("A.dot(B) = \n", A.dot(B), "\n\n")
print("Matrix Product\n\n")