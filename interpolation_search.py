def interpolation_search(arrr, arrr_size, toFind):
	low = 0
	high = arrr_size

	while low <= high and toFind >= arrr[low] and toFind <= arrr[high]:
		# print 'In while'
		pos = low + ((high-low) / (arrr[high]-arrr[low]) * (toFind - arrr[low]))
		print low
		if arrr[pos] == toFind:
			print 'Found!'

		if arrr[pos] < toFind:
			low = pos + 1
		else:
			high = pos - 1

arrr =  [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47];
toFind = 42
interpolation_search(arrr, len(arrr)-1, toFind)