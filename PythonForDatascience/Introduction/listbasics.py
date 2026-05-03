# List basics

"""
The difference between list append and extend method is that append adds its argument as a single element to the end of a list,
while extend iterates over its argument adding each element to the list, extending the list.
"""

L = [1, 2, 3]
L.append([4, 5])        # append adds the list [4, 5] as a single element to the end of L
print(L)
L.extend([6, 7])        # extend iterates over the list [6, 7] and adds each element to the end of L
print(L)

A = ["hard Rock", "heavy metal", "grunge"]
B = A
print(A)
print(B)

"""
Since B is referening to the same list as A, any changes made to the list through B will also affect A or vice versa. This is because 
both A and B are pointing to the same list in memory. If we want to create a new list that is a copy of A, 
we can use the copy() method or the list() constructor.
"""

A[0] = "pop"
print(A)
print(B)

"""
Now let's create a new list C by copying values of A and the modify the first element of C to "hip hop". 
This will not affect A or B since C is a new list that is independent of A and B.
"""

C = A[:]
print(C)

"""
Now let us change the first element of C to "hip hop" and see how it affects A and B.
"""

C[0] = "hip hop"
print(C)
print(A)
print(B)