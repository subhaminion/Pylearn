# aaaaabbbbcccdde
def encodeTheString(text):
	count         = 1
	encodedString = ""
	for x in xrange(0,len(string)):
		if x + 1 < len(string) and string[x] == string[x + 1]:
			count = count + 1
		else:
			encodedString = encodedString + string[x] + str(count)
			count         = 1
	print encodedString

string        = raw_input('Enter the String You want to manipulate: \n')
encodeTheString(string)