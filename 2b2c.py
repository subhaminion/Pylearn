# aaaaabbbbcccdde
def encodeTheString(string):
	if string is None or not string:
		return string
	count         = 1
	encodedString = ""
	for x in range(0, len(string)):
		if x + 1 < len(string) and string[x] == string[x + 1]:
			count = count + 1
		else:
			encodedString = encodedString + string[x] + (str(count) if count > 1 else '')
			count         = 1

	return encodedString if len(encodedString) < len(string) else string

string        = input('Enter the String You want to manipulate: \n')
print (encodeTheString(string))