import numpy as np
from primegen import gen_primes


def dixon(n,t=5):
	
	base = gen_primes(t)
	print(f"Done generating factor base: {base}")

	for i in range(1,t+1):
		print(f"{i} ")


if __name__ == "__main__":
    print("fuck")
    