import numpy as np
from numpy import pi

def my_function(x,y):
    return 10 * x + y

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

a = np.arange(10) ** 3

print("a = ", a)
print("a[2] = ", a[2])
print("a[2:5] = ", a[2:5])

a[:6:2] = 1000

print("new a = ", a)
print("reverse a = ", a[::-1])
print("Iteration of a, each element a[i] = i ** (1/3):\n\n")

for i in a:
    print(i ** (1 / 3))

j = my_function(5,4)
print(j)   

b = np.fromfunction(my_function,(5,4), dtype=int)

print("b from function f = ", b)
print("b[2,3] = ", b[2,3])
print("b[0:5, 1] = ", b[0:5,1])
print("b[:, 1] = ",b[:, 1])
print("b[1:3, :] = ", b[1:3, :])
print ("b[-1] = ", b[-1], "\n\n")

c = np.array([[[0, 1, 2],
               [10,12,13]],
              [[100, 101, 102],
               [110, 112, 113]]])
               
print("c.shape = ",c.shape)

print ("c[1, ...] = ", c[1, ...])

print("c[..., 2] = ", c[..., 2])