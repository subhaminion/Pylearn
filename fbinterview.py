# Given an unsorted array, sort it in such a way that the first 
# element is the largest value, the second element is the smallest, 
# the third element is the second largest element and so on.
# 1, 2, 3, 4, 5
# [2, 4, 3, 5, 1] -> [5, 1, 4, 2, 3] 
# can you do it without using extra space 
# public void sortAlternate(int[] nums){}


import random
# arrr = random.sample(range(0, 20), 10)
arrr = [2,4,3,5,1]
finList = []
arrr.sort()
for i in arrr:
	for j in reversed(arrr):
		print j