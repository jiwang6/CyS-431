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

	R = t+1


	for i in range(R): # generate 2*t good equations
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

		print(f"{i} {lhs}^2 == {rhs} {EV}")

	g_mat = np.delete(g_mat, 0, 0)

	g_mod = g_mat % 2

	index_set = list(range(R))

	for L in range(1,R+1):
		print(f"choosing {L}")
		for subset in itertools.combinations(index_set, L):
			sum_arry = np.zeros(t)
			lhs_prod = 1
			rhs_prod = 1
			for i in subset:
				sum_arry += g_mod[i]
				lhs_prod *= good_LHS[i]
				rhs_prod *= good_RHS[i]
			sum_arry = sum_arry % 2
			if np.all(sum_arry == 0):
				x = lhs_prod % n
				y = isqrt(rhs_prod) % n
				yp = (-1 * y) % n
				if x not in [y, yp]:
					print( gcd(abs(x-y), n))



""" 
	for L in range(R+1):
		for subset in itertools.combinations(g_mod, L+1):
			print(subset)
			sum_arry = np.asarray(subset).sum(axis= 0)
			print(sum_arry)
			mod_arry = sum_arry % 2
			if np.all(mod_arry==0): 
"""
				


if __name__ == "__main__":
	print(dixon(388616539515299129, 70))
    
