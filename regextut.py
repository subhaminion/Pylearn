import re
pattern = re.compile(r"\w+")
string = "regex is awesome"
result = pattern.match(string)
print result.group()