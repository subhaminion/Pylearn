print("Welcome to Mad Libs - Python Edition. Follow the prompts to create your own hilarious story.")

proper_name1 = raw_input("Enter a name: ")
proper_name2 = raw_input("Enter another name: ")
noun1        = raw_input("Enter a proper title: ")
place1       = raw_input("Enter a place: ")
place2       = raw_input("Enter another place: ")
verb1        = raw_input("Enter a present-tense verb: ")
noun3        = raw_input("Enter a noun: ")
noun2        = raw_input("Enter a plural noun: ")
noun4        = raw_input("Enter another plural noun: ")
num2         = raw_input("Enter a number: ")
num1         = raw_input("Enter another number: ")
percent1     = raw_input("Enter another number: ")

print("Dear {}, It is my pleasure to {} to you today. I am {} and I'm the "
      "{} of {}. I have inherited {} {} but I need your help to get it to {}. "
      "Please send me your {} and the sum of {} {} to get started, and I will "
      "give you {} percent of my inheritance. Yours truly, {}".format(
          proper_name1, verb1, proper_name2, noun1, place1, num1, noun2, 
          place2, noun3, num2, noun4, percent1, proper_name2))