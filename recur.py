# def calc_factorial(x):
# 	if x == 1:
# 		return 1
# 	else:
# 		return (x * calc_factorial(x-1))


# print(calc_factorial(4))

def fac(x):
	if x==1:
		return 1
	else:
		return (x * fac(x-1))

num = 4
print (fac(num))