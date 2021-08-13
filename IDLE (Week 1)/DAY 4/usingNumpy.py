import numpy as np

'''
verbs = np.array(["Walk", "Jump", "Climb"])
endings = np.array(["ed", "ing"])
 
verbs = np.reshape(verbs, (3, 1))
 
verbs_and_endings = np.char.add(verbs, endings)
 
print(verbs_and_endings)
'''
'''
array_a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(array_a)

print(array_a[0, 0])
print(array_a[1, 2])
print(array_a[2, 0])
print(array_a[2, 3])
'''
 
array_a = np.array([[1,2], [3,4], [5,6]])
 
bigger_than_two = array_a[array_a > 2]
 
print(bigger_than_two)
