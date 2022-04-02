import random
import math

def brute_force(n):
	upper_lim = math.isqrt(n)
	print(upper_lim)

	if (n%2==0):
		return(2)

	for i in range(3,upper_lim+1,2):
		if (n%i==0):
			return(i)

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
	challenge = 213016805697990920376675714115937442919
	print(brute_force(167))