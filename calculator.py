def add(num1, num2):
	return num1 + num2

def minus(num1, num2):
	return num1 - num2

def divide(num1, num2):
	return num1 / num2

def multiply(num1, num2):
	return num1 * num2


run = True
# choice = 0
while run:
	print 'Select An Option'
	print '1 for addition'
	print '2 for substraction'
	print '3 for division'
	print '4 for multiplication'
	print '5 for exit'
	choice = input('Enter a choice 1/2/3/4/5: ')

	if choice == 1:
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print add(num1, num2)
	if choice == 2:
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print minus(num1, num2)
	if choice == 3:
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print divide(num1, num2)
	if choice == 4:
		num1 = int(input("Enter first number: "))
		num2 = int(input("Enter second number: "))
		print multiply(num1, num2)
	if choice == 5:
		print 'Bye!'
		run = False
		