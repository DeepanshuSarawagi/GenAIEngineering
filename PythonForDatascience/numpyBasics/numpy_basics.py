import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1d)
print(type(arr1d))
print(arr1d.shape) # Print the shape of the array (number of elements in each dimension)
print(arr1d.dtype) # Print the data type of the array elements
print(arr1d.ndim)  # Print the number of dimensions of the array
print(arr1d.size)  # Print the total number of elements in the array

"""Following is the illustration how numpys are successful. To perform mathematical operations on arrays, we can use the built-in 
functions provided by NumPy. These functions are optimized for performance and can operate on entire arrays at once, 
which is much faster than using loops in Python."""

u = [1,0]
v = [0,1]

z = []

for n, m in zip(u, v):
    z.append(n + m)

print(z)

"""The above same operaiton can be performed using numpy as follows. This is much faster and more efficient than the previous method."""

u = np.array([1,0])
v = np.array([0,1])
z = u + v
print(z)