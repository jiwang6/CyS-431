import numpy as np
from math import sqrt, gcd
import itertools
import random
import math
import sympy
from primegen import gen_primes


def brute_force(n):
	upper_lim = math.isqrt(n)

	if (n % 2 == 0):
		return(2)

	return next((i for i in list(sympy.primerange(upper_lim)) if (n % i == 0)), -1)


def pollard_rho(n, seed=3, f=lambda x: x**2 + 1):
	a, b, d = seed, seed, 1
	while d == 1:
		a = f(a) % n
		b = f(f(b)) % n
		d = math.gcd((a - b) % n, n)
		m = n/d
	return (d, a, b) if d != n and m.is_integer else (-1, -1, -1)


def dixon(n,t=5):
	
	base = gen_primes(t)z
	print("Done generating factor base.")

	for i in range(1,t+1):
		print(f"{i} ")



if __name__ == "__main__":  # main funciton loop
	tests = [1762741, 6937031, 3572694269, 498587077741,
			 388616539515299129, 24232273352113381895280635789,
			 213016805697990920376675714115937442919]
	#curr_test = tests[int(input("case? ")) % 7]
	curr_test = tests[0]

	print(f"testing {curr_test}")

	print(f"brute: factor = {brute_force(curr_test)}")

	print(f"rho: factor = {pollard_rho(curr_test)}")

	print(f"Dixon: factor = {dixon(curr_test)}")