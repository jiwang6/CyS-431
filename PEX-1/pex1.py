import time

import signal

from factorAlgos import brute_force, pollard_rho, fast_MR

print("PEX1 - Factoring! - by Cadet Awesomesauce \nCyS 431")

def test_algo(function, attempts = 3, time = 2):
	return 0

def main():
	print("PEX1 - Factoring! - by Cadet Awesomesauce \nCyS 431")

	while True: # main driver funct

		while True:
			number = input("Enter a number (0 to exit): ")
			try:
				n = int(number)
				if n < 0: 
					print("Sorry, input must be a positive integer, try again")
					continue
				break
			except ValueError:
				print("That's not an int!")


		if n == 0:
			break

		print("Brute force factoring: ")

if __name__ == "__main__":
	main()