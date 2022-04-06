from timeout import attempt_factor
from factorAlgos import brute_force, pollard_rho, dixon

def main():
	print("PEX1 - Factoring! - by C/Wang \nCyS 431")

	while True: # main driver funct
		cases = []
		while True:
			number = input("Enter a number (0 to exit, -1 for test cases): ")
			try:
				n = int(number)
				if n < -1: 
					print("Sorry, input must be a positive integer, try again")
					continue
				break
			except ValueError:
				print("That's not an int!")

		if n == -1:
			cases = [1762741, 6937031, 3572694269, 498587077741,
				388616539515299129, 24232273352113381895280635789,
				213016805697990920376675714115937442919]
		elif n == 0:
			break
		else:
			cases.append(int(number))
		for test_num in cases:
			print(f"\n\nFactoring: {test_num}")

			print("\nBrute force factoring")
			factor, time = attempt_factor(test_funct = brute_force, test_prime = test_num, attempt_count = 1, t_limit=2)
			if factor == -1:
				print(f"{test_num} appears to be prime.")
			elif factor != -2:
				time = "{:.2f}".format(time)
				print(f"Found a factor = {factor}\nIt took {time} seconds.")

			print("\nPollard's Rho")
			factor_arry, time = attempt_factor(test_funct = pollard_rho, test_prime = test_num, attempt_count = 3, t_limit=2)
			if factor_arry == -2:
				continue
			elif factor_arry[0] == -1:
				print(f"{test_num} appears to be prime.")
			else:
				factor, a, b = factor_arry[0], factor_arry[1], factor_arry[2]
				time = "{:.2f}".format(time)
				print(f"Found a factor = {factor}\na = {a}, b = {b}\nIt took {time} seconds.")






if __name__ == "__main__":
	main()