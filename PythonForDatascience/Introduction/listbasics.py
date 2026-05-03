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