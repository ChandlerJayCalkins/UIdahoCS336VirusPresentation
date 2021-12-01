import sys

# checks to make sure that the commandline argument is valid
def handle_input(max):
	if not max.isdigit():
		print("Invalid argument, must be a positive integer greater than 1")
	else:
		max = int(max)
		if max < 2:
			print("Invalid argument, must be a positive integer greater than 1")
		else:
			calc_primes(max)

# calculates prime numbers and outputs them
def calc_primes(max):
	# if max is an integer greater than or equal to 2, then proceed
	if isinstance(max, int):
		if max >= 2:
			# wipes the contents of the last primes.txt file if there was one
			with open("primes.txt", "w") as file:
				file.truncate(0)

			# opens an iostream to write prime numbers to a file
			with open("primes.txt", "a") as file:
				# writes 2 in by default
				file.write("2")
				print("2")

				# if the user wants prime numbers bigger than 2 to be printed
				if (max > 2):
					# loop through each odd number up to max, test to see if it's divisble by all odd numbers below 1/2 of itself
					for p in range(3, max+1, 2):
						for d in range(3, int(p/2), 2):
							# if  p is divisble by d, then p is not prime
							if p % d == 0:
								break
						# if p is not divisible by any odd numbers up to half of itself, then p is prime
						else:
							file.write("\n" + str(p))
							print(str(p))

# gets the max prime number from the user and handles argument errors
if (len(sys.argv) > 1):
	handle_input(sys.argv[1])
else:
	print("No argument, must give a positive integer greater than 1")