import random

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
		
		if y == 1 or y == n - 1:
			continue
		for _ in range(s - 1):
			y = pow(y, 2, n)
			if y == n - 1:
				break
		else:
			return False
	return True

for i in [17,36,43]:
	print(f"{i} is Prime" if miller_rabin(i,10) else f"{i} is not Prime", end = "\n\n\n")