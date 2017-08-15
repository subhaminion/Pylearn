def html_tag(tag):
	print tag
	def wrap_text(msg):
		print ('<{0}>{1}</{0}>'.format(tag, msg))

	return wrap_text

print_h1 = html_tag('h1')
print_h1()