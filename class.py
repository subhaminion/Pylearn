# class firstClass:
# 	"""docstring for firstClass"""
# 	# def __init__(self, arg):
# 	# 	super(firstClass, self).__init__()
# 	# 	self.arg = arg
# 	var = 10
# 	def classFunc(self):
# 			print self
# 			print 'Coming from class'

# print firstClass.var

# print firstClass.classFunc

# objMadafaka = firstClass()

# print objMadafaka.var

# print objMadafaka.classFunc

class Constructor(object):
	"""docstring for Constructor"""
	def __init__(self, r = 0, i = 0):
		self.real = r
		self.imag = i
	def getData(self):
		print ("{0}+{1}j".format(self.real, self.imag))

obj = Constructor(2, 3)

obj.getData()

newObj = Constructor(5)

newObj.attr = 10
print obj.__dict__
print ((newObj.real, newObj.imag, newObj.attr))