import sys
class Employee(object):
	raise_amnt = 1.04
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def fullname(self):
		return "{} {}".format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amnt)

class Developer(Employee):
	def __init__(self, first, last, pay, prog_lang):
		super(Developer, self).__init__(first, last, pay)
		self.prog_lang = prog_lang


print (help(Developer))
sys.exit()
obj1 = Developer('Subham', 'Bhattacharjee', 11000, 'NodeJs')
print obj1.pay
obj1.apply_raise()
print obj1.fullname()
print obj1.prog_lang