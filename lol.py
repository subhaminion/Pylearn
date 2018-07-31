# class Person:
# 	def say_hi(self):
# 		print('Hello, how are you?')
# p = Person()
# p.say_hi()
def decoratior(fn):
	def inner(n):
		return fn(n) + 1
	return inner

@decoratior
def f(n):
	return n+1

f = decoratior(f)
print (f(5))