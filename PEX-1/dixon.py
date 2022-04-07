import numpy as np
from primegen import gen_primes
import random
from math import isqrt, gcd
import itertools

def dixon(n,t=5):
	
	base = gen_primes(t)
	print("Done generating factor base.")

	good_LHS, good_RHS, bad_LHS= [], [], []
	g_mat = np.zeros(t)

	R = t


	for j in range(R): # generate 2*t good equations
		good_eq = False
		k = 0
		while not good_eq:
			k +=1
			EV = np.zeros(t)

			lhs = isqrt(k*n) + 1
			if lhs in good_LHS + bad_LHS: # eliminate duplicates
				continue

			rhs = pow(lhs,2,n)
			if rhs in [0,1]:
				continue # if rhs is stupid

			test_rhs = rhs

			for b_index in range(t): # for each base in prime base
				while test_rhs % base[b_index] == 0: 
					test_rhs /= base[b_index]
					EV[b_index] +=1 
			if test_rhs == 1:
				good_eq = True
			else:
				bad_LHS.append(lhs)

		good_LHS.append(lhs)
		good_RHS.append(rhs)
		g_mat = np.vstack([g_mat, EV])

		print(f"{j} {lhs}^2 == {rhs} {EV}")

	g_mat = np.delete(g_mat, 0, 0)

	g_mod = g_mat % 2

	index_set = list(range(R))
	combo_range = list(range(1,R+1))

	a = np.array(range(int(R/2) + 2))
	b = -1 * np.array(range(1,int(R/2 + 2)))

	c = np.array(list(zip(a,b)))
	c = c.flatten()[:-1]

	for i in c:
		L = combo_range[i]
		print(f"choosing {L}, index {i}")
		for subset in itertools.combinations(index_set, L):
			sum_arry = np.zeros(t)
			lhs_prod = 1
			rhs_prod = 1
			for j in subset:
				sum_arry += g_mod[j]
				lhs_prod *= good_LHS[j]
				rhs_prod *= good_RHS[j]
			sum_arry = sum_arry % 2
			if np.all(sum_arry == 0):
				x = lhs_prod % n
				y = isqrt(rhs_prod) % n
				yp = (-1 * y) % n
				if x not in [y, yp]:
					return( gcd(abs(x-y), n))


if __name__ == "__main__":
	print(dixon(388616539515299129, 1400))
    
