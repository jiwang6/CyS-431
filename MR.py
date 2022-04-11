import random

def miller_rabin(n):
	k, m = 0, n - 1
	while m % 2 == 0:
		k += 1
		m //= 2

	print(f"{n} - 1 = 2^{k} * {m}\n")

	if n == 2:
		return True
	if n % 2 == 0:
		return False

	for i in range(n):
		a = random.randrange(2, n-1)
		#a = 19
		b = pow(a,m,n) if i ==0 else pow(b,2,n)

		print(f"b_{i} = {b} (mod {n})")

		if i == 0 and b in [-1, 1]:
			return True

		if b == 1:
			return False
		elif b == -1:
			return True
		
		if i == n-1 and b != -1:
			return False

n = 81

print(f"{n} is Prime" if miller_rabin(n) else f"{n} is not Prime", end = "\n\n")