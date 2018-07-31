# Find whether an array is subset of another array | Added Method 3
# Given two arrays: arr1[0..m-1] and arr2[0..n-1].
# Find whether arr2[] is a subset of arr1[] or not.
# Both the arrays are not in sorted order. It may be assumed that elements in both array are distinct.
# Examples:
# Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
# Output: arr2[] is a subset of arr1[]

# Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
# Output: arr2[] is a subset of arr1[]

# Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3}
# Output: arr2[] is not a subset of arr1[]

# The Function which does the thing Bitch ;) But it is not a proper solution
# A proper solution uses hashing
# def isSubset(arr1, arr2):
# 	for x in xrange(0,len(arr2)):
# 		for z in xrange(0,len(arr1)):
# 			if arr2[x] == arr1[z] and x == z:
# 				return True
# 			else:
# 				return False

# arr1 = [11, 1, 13, 21, 3, 7]
# arr2 = [11, 3, 7, 1]

# print 'Generating results form the normal solution'
# print isSubset(arr1, arr2)

# hashedArr = map(hash, arr1)
# # for y in xrange(0,len(arr1)):
# # 	hashedArr[y] = arr1[y]
# print hashedArr



# from datetime import datetime

# #assuming time format comes in a string like this: '8:30:00'
# #assumming provided time has sense, i.e. end1 > start1 and end2 > start2

# TIME_FORMAT = '%H:%M:%S'

# def overlap(start1, end1, start2, end2):
#     #transform time        
#     start1_time = datetime.strptime(start1, TIME_FORMAT )
#     end1_time = datetime.strptime(end1, TIME_FORMAT )
#     start2_time = datetime.strptime(start2, TIME_FORMAT )
#     end2_time = datetime.strptime(end2, TIME_FORMAT )

#     #checking conditions
#     if (min(start1_time, end1_time) <= max(start2_time, end2_time)) \
#     and \
#     (max(start1_time, end1_time) >= min(start2_time, end2_time)):
#         return True
#     else:
#         return False


# print(overlap('8:30:00', '9:30:00', '8:45:00', '10:00:00'))
a0, a1, a2, b0, b1, b2 = 5, 6, 7, 3, 6, 10
alicepoints = 0
bobpoints = 0
aTupple = [a0, a1, a2]
bTupple = [b0, b1, b2]
for i,j in zip(aTupple, bTupple):
    if i < j:
        bobpoints += 1
    elif i > j:
        alicepoints += 1


print (alicepoints, bobpoints)