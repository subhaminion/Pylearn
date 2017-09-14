def user_info(user):
	return 'Name: {user.name} Age: {user.age}'.format(user=user)

class StringCheck(object):
	def __init__(self):
		self.name = 'subham'
		self.age = 22

user = StringCheck()
print user_info(user)
print (user)