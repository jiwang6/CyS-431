import numpy as np
from primegen import gen_primes
import random


def dixon(n,t=5):
	
	base = gen_primes(t)
	print("Done generating factor base.")

	good_LHS =[]
	
	for _ in range(t):
		new_int = random.randint(2,n-1)
		while new_int in good_LHS: # prevents dup
			new_int = random.randint(2,n-1)
		good_LHS.append(new_int)

	good_RHS = [pow(i,2,n) for i in good_LHS]

	print(base)
	print(good_LHS)
	print(good_RHS)

	g_matrix = np.zeros(t)

	for rhs in good_RHS:
		EV = np.zeros(t)

		for b_index in range(t):
			while rhs % base[b_index] == 0:
				rhs /= base[b_index]
				EV[b_index] +=1
		print(EV)


	print(g_matrix)
	print(good_RHS)


if __name__ == "__main__":
	dixon(187, 10)
    