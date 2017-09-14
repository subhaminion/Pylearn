class Employee(object):
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super(Developer, self).__init__(first, last, pay)
		self.prog_lang = prog_lang


class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super(Manager, self).__init__(first, last, pay)

		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print ('--->', emp.fullname())


dev_1 = Developer('Subham', 'Bhattacharjee', 100000, 'Python')
dev_2 = Developer('Subham', 'Bhattacharjee', 100000, 'Python')
mgr_1 = Manager('Mark', 'Zuckerberg', 3546546, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)

mgr_1.remove_emp(dev_1)

mgr_1.print_emp()