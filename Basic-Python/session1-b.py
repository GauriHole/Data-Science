''' -------Copy ------'''
import copy
original_list = [1, [2, 3], 4 ]
shallow_copy = copy.copy(original_list)

print("Original List : ", original_list)
print("Shallow Copy Before Modify : ", shallow_copy)

shallow_copy[1][0] = 99
print("Original list : ", original_list)
print("Shallow Copy Before Modify : ", shallow_copy)

original_list = [1, 2, 3, 4, 5]
