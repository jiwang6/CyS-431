import numbthy as nt
import random
import math
import time


def brute_factor(n):
	up_bound =  math.floor(pow(n,1/2))
	for i in range(1,up_bound+1):
		if n % i == 0:
			return i

def pollard_rho(n, factor_arry, seed=2, f=lambda x: x**2 + 1):
	a, b, d = seed, seed, 1
	while d == 1:
		a = f(a) % n
		b = f(f(b)) % n
		d = math.gcd((a - b) % n, n)
		m = n/d
	if d != n and m.is_integer:
		print(f"factor p = {d} found; a = {a}, b = {b}")

		factor_arry.append(d)
		pollard_rho(int(m), factor_arry)
	else:
		factor_arry.append(d)

	


def miller_rabin(n, t):
	s, r = 0, n - 1
	while r % 2 == 0:
		s += 1
		r //= 2

	print(f"{n} = 2^{s} * {r} + 1")

	if n == 2:
		return True
	if n % 2 == 0:
		return False

	print("good equations:")
	for _ in range(t):
		a = random.randrange(2, n - 1)
		y = pow(a, r, n)
		print(f"{y} = {a}^{r} (mod {n})")

		if y in [1, n - 1]:
			continue
		for _ in range(s - 2):
			y = pow(y, 2, n)
			if y == n - 1:
				break
		else:
			return False
	return True

	

if __name__ == "__main__": # main funciton loop
	print("PEX1 - Factoring! - by Cadet Awesomesauce \nCyS 431")
	print(brute_factor(16))
	""" 
	n = 124076833
	factors = []

	start_time = time.time()
	pollard_rho(n, factors)
	print(f"--- Pollard's Rho took: {time.time() - start_time} seconds ---")
	print(f"for n = {n}, we have factors: {factors}")


	i = n
	print(f"{i} is Prime" if miller_rabin(i,5) else f"{i} is not Prime", end = "\n\n")
	 """