import signal
import time
from factorAlgos import pollard_rho

class timeout:
	def __init__(self, seconds=1, error_message='Timeout'):
		self.seconds = seconds
		self.error_message = error_message
	def handle_timeout(self, signum, frame):
		raise TimeoutError(self.error_message)
	def __enter__(self):
		signal.signal(signal.SIGALRM, self.handle_timeout)
		signal.alarm(self.seconds)
	def __exit__(self, type, value, traceback):
		signal.alarm(0)

def run_forever():
	second = 0
	while(1):
		print(f"{second} seconds have passed")
		time.sleep(1)
		second += 1

def attempt_factor(attempt_count = 3, t_limit = 120, test_funct = run_forever, test_prime = None, f_base = False):
	for i in range(attempt_count):
		try:
			if f_base:
				f_input = int(input("Enter # of factors in factor base: "))
				start_time = time.time()
				with timeout(seconds = t_limit):
					return test_funct(test_prime, f_input), time.time() - start_time
			else:
				start_time = time.time()
				with timeout(seconds = t_limit):
					return(test_funct(test_prime)), time.time() - start_time
		except Exception:
			print(f"Attempt {i+1} failed to factor in under {t_limit} seconds")
	return -2, -2

if __name__	== "__main__":	
	print(attempt_factor(t_limit = 120, test_funct = pollard_rho, test_prime=1762741))