
# 1. Import numpy as np

import numpy as np  
import shutil

def pretty(x, problemStatement):
    
    # Get terminal width
    terminalWidth = shutil.get_terminal_size().columns
    
    # Define character to use for the line
    lineCharacter = '='
    
    if (x != -1):
        print(x, ".  ", problemStatement, "\n\n")
       
    else:
        print("\n",(lineCharacter *(terminalWidth - 1)), "\n\n")
        
    return
    

# 2. Print the numpy version and configuration

pretty(2, "Print the numpy version and the configuration")

print(np.__version__)
print(np.show_config())

pretty(-1,"")

# 3. Create a null vector of size 10

pretty(3, "Create a null vector of size 10.")

nullVec = np.zeros(10, dtype=int)

print("nullVec = ", nullVec)
pretty(-1, "")

# 4. How to find the memory size of an array

pretty(4, "How to find the memory size of an array?")

a = np.arange(10)

print("a = ", a)
print("Size according to a.nbytes = ", a.nbytes)
print("Alternatively, calculate the size of a manually.")

numElements = a.size
itemSize = a.itemsize

memorySizeA = numElements * itemSize

print("a.size * a.itemsize = ", memorySizeA)
pretty(-1,"")

# 5. How to get the documentation of the numpy add function from the command line?

pretty(5, "How to get the documentation of the numpy add function from the command line?")

print("In the interpreter, type help(np.add).  This will show the documentation.")
pretty(-1,"")

# 6.  Create a null vector of size 10 but the fifth value which is 1

pretty(6, "Create a null vector of size 10 but the fifth value which is 1")

newVec = np.zeros(10, dtype = int)
newVec[4] = 1

#slower version
slowVec = (np.arange(10) == 4).view(np.uint8)

print("newVec = ", newVec)
print("slowVec = ", slowVec)
pretty(-1, "")

# 7. Create a vector with values ranging from 10 to 49

pretty(7, "Create a vector with values ranging from 10 to 49")

v = np.arange(10,50)

print("v = ", v)
pretty(-1, "")

# 8. Reverse a vector

pretty(8, "Reverse a vector.")

print("v[::-1] = ", v[::-1])
pretty(-1,"")

#9.  Create a 3x3 matrix with values ranging from 0 to 8

pretty(9, "Create a 3x3 matrix with values ranging from 0 to 8")

m = np.array([[[0, 1, 2], [3, 4, 5], [6, 7, 8]]])

print ("m = ", m)
pretty(-1, "")

#10. Find indices of non-zero elements from [1, 2, 0, 0, 4, 0]

pretty(10, "Find indices of non-zero elements from [1, 2, 0, 0, 4, 0]")

m = np.array([1, 2, 0, 0, 4, 0])
indices = np.array([], dtype=int)
index = 0

for i in m:
    if (i != 0):
        indices = np.append(indices, index)
    index += 1
    
print("Indices = ", indices)
pretty(-1, "")

# 11. Create a 3x3 identity matrix

pretty(11, "Create a 3x3 identity matrix")

id = np.identity(3, dtype=int)

print("id = ", id)
pretty(-1, "")

# 12. Create a 3x3x3 array with random values

pretty(12, "Create a 3x3x3 array with random values")

rg = np.random.default_rng(1)
m = rg.random(27).reshape(3,3,3)

print("m = ", m)
pretty(-1, "")

# 13. Create a 10x10 array with random values and find the minimum and maximum values

pretty(13, "Create a 10x10 array with random values and find the minimum and maximum values")

rg = np.random.default_rng(100)
a = rg.random(100).reshape(10,10)

print("a = ", a, "\n")
print("np.max(a) = ", np.max(a))
print("np.min(a) = ", np.min(a))
pretty(-1, "")

# 14. Create a random vector of size 30 and find the mean value

pretty(14, "Create a random vector of size 30 and find the mean value")

rg = np.random.default_rng(100)
v = rg.random(30)

print("v = ", v, "\n")
print("np.mean(v) = ", np.mean(v))
pretty(-1, "")

# 15. Create a 2D array with 1 on the border and 0 on the inside

pretty(15, "Create a 2D array with 1 on the border and 0 on the inside")

m = np.ones((5,5), dtype = int)

m[1:-1, 1:-1] = 0

print("m = ", m)
pretty(-1, "")

# 16. How to add a border (filled with 0's) around an existing array








    