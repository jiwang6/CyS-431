import signal, time, sympy

""" def handler(signum, frame):  # sourcery skip: raise-specific-error
	print("failed to factor under 2 min!")
	raise Exception("it don't work")

def loop_forever():
	while 1:
		print("tick")
		time.sleep(1)

signal.signal(signal.SIGALRM, handler)
signal.alarm(10)

try:
	loop_forever()
except Exception e:
	print(e)

 """

print(list(sympy.primerange(10)))