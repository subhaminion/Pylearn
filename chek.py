import random
def partition(arrlist, low, high):
	i = (low - 1)
	pivot = arrlist[high]
	for j in xrange(low, high):
		if arrlist[j] <= pivot:
			i = i + 1
			arrlist[i], arrlist[j] = arrlist[j], arrlist[i] #swapping like a pro in python

	arrlist[i+1], arrlist[high] = arrlist[high], arrlist[i+1]
	return ( i + 1 )

def quicksort(arrlist, low, high):
	print 'Hit!'
	if low < high:
		piv = partition(arrlist, low, high)
		quicksort(arrlist, low, piv - 1)
		quicksort(arrlist, piv + 1, high)

# arrlist = random.sample(range(0, 20), 15)
arrlist = [1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4]
print "Unsorted Array: "
print arrlist
quicksort(arrlist, 0, len(arrlist)-1)
print "Sorted Array: "
print arrlist