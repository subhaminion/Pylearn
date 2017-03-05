number = 213;
guess = int(raw_input("Enter your Guess: "))

if guess == number:
	print("Your entered a right value")
elif guess < number:
	print("It is less")
else:
	print("Meh!")