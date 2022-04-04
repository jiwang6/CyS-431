import numpy as np
from math import sqrt, gcd
import itertools
import random
import math


def brute_force(n):
    upper_lim = math.isqrt(n)
    # print(upper_lim)

    if (n % 2 == 0):
        return(2)

    for i in range(3, upper_lim+1, 2):
        if (n % i == 0):
            return(i)


def pollard_rho(n, seed=3, f=lambda x: x**2 + 1):
    a, b, d = seed, seed, 1
    while d == 1:
        a = f(a) % n
        b = f(f(b)) % n
        d = math.gcd((a - b) % n, n)
        m = n/d
    return (d, a, b) if d != n and m.is_integer else (-1, -1, -1)


def fast_MR(n, t):
    s, r = 0, n - 1
    while r % 2 == 0:
        s += 1
        r //= 2

    #print(f"{n} = 2^{s} * {r} + 1")

    if n == 2:
        return True
    if n % 2 == 0:
        return False

    #print("good equations:")
    for _ in range(t):
        x = random.randrange(2, n - 1)
        y = pow(x, r, n)
        print(f"{y} = {x}^{r} (mod {n})")

        if y in [1, n - 1]:
            continue
        for _ in range(s - 2):
            y = pow(y, 2, n)
            if y == n - 1:
                break
        else:
            return math.gcd(abs(x-y), n)
    return -1

def dixon(n):

    base = [2, 3, 5, 7]

    start = int(sqrt(n))

    pairs = []

    for i, item in itertools.product(range(start, n), base):
        lhs = i**2 % n
        rhs = item**2 % n

        if (lhs == rhs):
            pairs.append([i, item])

    new = []

    for pair in pairs:
        factor = gcd(pair[0] - pair[1], n)

        if(factor != 1):
            new.append(factor)

    x = np.array(new)
    return(np.unique(x))


if __name__ == "__main__":  # main funciton loop
    tests = [1762741, 6937031, 3572694269, 498587077741,
             388616539515299129, 24232273352113381895280635789,
             213016805697990920376675714115937442919]
    curr_test = tests[0]

    print(f"testing {curr_test}")
    # print(brute_force(curr_test))
    d, a, b = pollard_rho(curr_test)
    print(f"d = {d}, a = {a}, b = {b}")

    print(fast_MR(curr_test, 30))

    #div = curr_test/d
    #print(f"{d} * {div} = {curr_test}")
