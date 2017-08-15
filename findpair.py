import random
arrr = [1,2,3,4,5,6,7,8,9]
# arrr = random.sample(range(0, 20), 10)
print arrr
arrr.sort()
diff = 2
for i in xrange(len(arrr)):
	for indexVal in xrange(len(arrr)):
		if (arrr[indexVal] + diff) == arrr[i]:
			print str(arrr[indexVal]) + ' ' + str(arrr[i])