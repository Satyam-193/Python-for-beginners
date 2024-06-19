
# List can be initialized in following ways
# First two list are empty list

l1 = list()
l2 = []

# l3 is One Dimensional Array
# l4 and l5 are Two Dimensional Array

l3 = [1,2,3,4]
l4 = [[1,2],[4,8]]
l5 = [[1,2,5],[4,8,10],[1,9,4]]

# to access the value of a particular index value in list we can search using there index as in form list[index].
# All index start from 0.
 Accessing Index [3], [1][1], [0][2]

print(l3[3]) # print 4
print(l4[1][1]) # print 8
print(l5[0][2]) # print 5

# to calculate mean of all the elements in list we can use numpy and its function.
# importing numpy module and declaring its reference as np.
import numpy as np

result = np.mean(l4)
# print 3.75
print(result) 

# we can also initialize list as in zeroes and ones using numpy as

list1 = np.zeros((3,3))
print(list1)
# print [[0,0,0], [0,0,0],[0,0,0]]

list2 = np.ones((2,2))
print(list2)
# print [[1,1],[1,1]]
