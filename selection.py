import random
def selectionSort(arr, n):
	for i in xrange(n):
		min = i
		for j in xrange(i+1, n):
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]


# array = random.sample(range(0, 20), 15)
array = [12,4,3,6,7,8,9,4,2,2,1,5]
selectionSort(array, len(array))

print array