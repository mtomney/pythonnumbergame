from random import randint
def num_game(): 
	name = raw_input("Welcome to the number guessing game. I May I have your name? ")
	print ("Weclome {}, in this game you will have 5 attempts to guess a number between 1 and 15.").format(name)
	print ("I have selected a number between 1 and 15, please guess the number!")
	magic_num = randint(1,15)
	guesses = 0
	while guesses < 6:
		user_guess = int(raw_input("Your number guess: "))
		guesses = guesses + 1
		if user_guess == magic_num:
			print "Correct, that was my number, great job!"
			return
		elif user_guess > magic_num:
			print "Too high! Guess a lower number"
		else:
			print ("Too low! Guess a higher number!")

		if user_guess != magic_num and guesses == 5:
			magic_num = str(magic_num)
			print ("Sorry {}, my number was " + magic_num + ". Better luck next round!").format(name)
			return
num_game()