from math import ceil, sqrt


def bsgs(Q, g, p):
    '''
    Solve for x in Q = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    m = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    print(f"m = {m}")

    # Store hashmap of g^{1...m} (mod p). Baby step.
    #tbl = {pow(g, i, p): i for i in range(m+1)}

    tbl = {}

    for j in range(m+1):
        e = pow(g,j,p)
        d = {e:j}

        print(f"{g}^{j} = {e} (mod {p})")

        tbl.update(d)

    c = pow(g, -1 * m, p)

    # Search for an equivalence in the table. Giant step.
    for i in range(m):
        y = (Q * pow(c, i, p)) % p

        print(f"{Q} * {g}^(-{m})^{i} = {y} (mod {p})")

        if y in tbl:
            x = i * m + tbl[y]
            print(f"x = {i} * {m} + {tbl[y]} = {x}")
            print(f"j = {i}, i = {tbl[y]}")
            return x

    # Solution not found
    return None


print(bsgs(7,3,29))