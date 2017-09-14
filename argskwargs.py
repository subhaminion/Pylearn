# Example of args
def test_var_args(f_arg, *argv):
	print "First normal arg:", f_arg

	for arg in argv:
		print "Another arg through *argv: ", arg

test_var_args('First Variable', 'Subham', 'Bhattacharjee', 'is', 'Cool!')


# Example of kwargs
def test_var_kwargs(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.iteritems():
			print "%s = %s" %(key, value)

test_var_kwargs(name="Subham")