import re
import sys

def isPrime(n):
	"""
	Return True if n is prime, False otherwise
	
	:param n: The number to check for primality
	:return: True or False
	"""
	return re.match(r'^1?$|^(11+?)\1+$', '1' * n) is None

def gen_primes(n):
	"""
	Generate a list of prime numbers less than n
	
	:param n: The number of primes you want to generate
	:return: A list of prime numbers.
	"""

	N = int(n)
	M = 100              
	l = []

	while len(l) < N:
		l += filter(isPrime, range(M - 100, M)) 
		M += 100                                

	return l[:N]