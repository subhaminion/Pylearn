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
def isSubset(arr1, arr2):
	for x in xrange(0,len(arr2)):
		for z in xrange(0,len(arr1)):
			if arr2[x] == arr1[z] and x == z:
				return True
			else:
				return False

arr1 = [1,6,3]
arr2 = [4,5,1,6,3,6]

print isSubset(arr1, arr2)