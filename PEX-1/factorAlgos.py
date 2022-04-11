import numpy as np
from math import isqrt, gcd
import random
import itertools
import sympy
from primegen import gen_primes


def brute_force(n):
	if n == 2:
		return -1
	if (n % 2 == 0):
		return(2)
		
	upper_lim = isqrt(n)

	return next((i for i in list(sympy.primerange(upper_lim+1)) if (n % i == 0)), -1)


def pollard_rho(n, f=lambda x: x**2 + 1):
	if n in [1,2,3]:
		return (-1, -1, -1)

	seed = random.randint(2,n-1)
	a, b, d = seed, seed, 1
	while d == 1:
		a = f(a) % n
		b = f(f(b)) % n
		d = gcd((a - b) % n, n)
		m = n/d
	return (d, a, b) if d != n and m.is_integer else (-1, -1, -1)


def gen_EV(n, t):
	base = gen_primes(t)
	print("Done generating factor base.")

	good_LHS, good_RHS, bad_LHS= [], [], []
	g_mat = np.zeros(t)
	R = t + 1

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
				continue

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

		print(f"{j+1} {lhs}^2 == {rhs} {EV}")

	return good_LHS, good_RHS, np.delete(g_mat, 0, 0)

def dixon(n,t=5):
	good_LHS, good_RHS, g_mat = gen_EV(n, t)

	R = t+1

	g_mod = g_mat % 2

	index_set = list(range(R))
	combo_range = list(range(1,R+1))

	a = np.array(range(int(R/2) + 2))
	b = -1 * np.array(range(1,int(R/2 + 2)))

	c = np.array(list(zip(a,b)))
	c = c.flatten()[:-1]

	for i in c:
		L = combo_range[i]

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

				eq_array = [i + 1 for i in subset]

				if x not in [y, yp]:
					print(f"combine eqs {eq_array}")
					return( gcd(abs(x-y), n))
	return -1


if __name__ == "__main__":  # main funciton loop
	tests = [1762741, 6937031, 3572694269, 498587077741,
			 388616539515299129, 24232273352113381895280635789,
			 213016805697990920376675714115937442919]

	curr_test = tests[0]

	print(f"testing {curr_test}")

	print(f"brute: factor = {brute_force(curr_test)}")

	print(f"rho: factor = {pollard_rho(curr_test)}")

	print(f"Dixon: factor = {dixon(curr_test, 10)}")