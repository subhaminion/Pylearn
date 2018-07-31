# Regular Expressions in Python 2.7
# .(dot) for any chracters
# \w word char in other words single characters in a word
# the difference between .(dot) and \w is dot matches everything including space and special chars but \w matches a word like a-z
# \w+ a whole word
# \d digit
# \s whitespace
#  \S Non-Whitespace matches every fucking thing
#  +1 or more
#  *0 or more
# \. for period character
import re

def find(pat, txt):
	match = re.search(pat, txt)
	if match:
		print match.group()
	else:
		print 'Not Found!'

find(r'(\w+)@(\w+)\.(\w+)', 'subham@gmail.com bhat@gmail.com bumba@gmail.com') #for email

find(r':\s\w\w\w', 'words: blah blah blah')

find(r'blah', 'words: blah blah blah')

find(r':\s\d\s\d\s\d\s\w+\s\s\d', 'digits: 1 2 3 lol123  4')

find(r'\d\s+\d\s+\d', '1  2     3 5   4 ')

find(r'.+', 'I\'m gonna fucking match everything')

find(r'\S+', 'Im gonna fucking match everything')

find(r'[\w.]+@[\w.]+', 'blah subham.b@gmail.com')

# find all repreating characters
import re
m = re.findall(r"([A-Za-z0-9])\1+", "abcdaa")
if m:
    print m[0]
else:
    print '-1'