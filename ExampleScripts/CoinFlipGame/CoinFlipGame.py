import random

# loops until user doesn't want to continue
loop = True
while loop:
	# gets user input
	print("Welcome to the coin flip game. Try to guess either heads or tails correctly to win!")
	guess = input("Enter your guess here (either heads or tails): ")
	guess = guess.lower()[:5]

	# keeps prompting for input until input is valid
	while guess != "heads" and guess != "tails":
		print("Invalid input, your guess must either be \'heads\' or \'tails\'")
		guess = input("Enter your guess here (either heads or tails): ")
		guess = guess.lower()[:5]

	# randomly generate either 0 or 1 to represent heads or tails
	flip = random.randrange(0, 2)
	if flip == 0:
		flip = "heads"
	else:
		flip = "tails"

	# prints the results to the player
	print(f"The result was {flip}")
	if guess == flip:
		print("You won!")
	else:
		print("You lost")

	# asks the user if they would like to play again or if they would like to quit
	print("Would you like to play again? Enter \'n\' to quit, press enter nothing to continue: ")
	loop = input() != 'n'