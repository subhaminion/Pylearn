class Employee(object):
	def __init__(self, rank, status):
		self.rank = rank
		self.status = status

	def recieveCall(self fromEmp):
		print 'Yay!! Got the call!'
	
	def passCall(self, toEmp):
		self.status = 'Engaged'


rank1 = Employee('Basic', 'Available')
rank2 = Employee('Supervisor', 'Available')
rank3 = Employee('DepartmentHead', 'Available')