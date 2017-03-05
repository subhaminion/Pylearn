arrr = [1, 7, 5, 9, 2, 12, 3]
arrr.sort()
diff = 2
for i in xrange(len(arrr)):
	for indexVal in xrange(len(arrr)):
		if (arrr[indexVal] + diff) == arrr[i]:
			print str(arrr[indexVal]) + ' ' + str(arrr[i])