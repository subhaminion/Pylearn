def search(arr, n, x):
	for i in xrange(0,n):
		if arr[i] == x:
			tosend = ""+str(x)+"  is present at index "+ str(i)+""
			return tosend

	return 'Sorry we coudn\' find your value'

arrr = [1, 2, 3, 4, 5, 8]
x = 4
n = len(arrr)

print search(arrr, n, x)