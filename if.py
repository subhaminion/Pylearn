number = 21
run = True

while run:
		guess = input('What is your guess!: ')
		if guess == number:
				print('You\' gussed it right!')
				run = False
		elif guess < number:
			print('Its a little higher!')
		else:
			print('Its a little lower')
else:
	print('This is the else block of while')