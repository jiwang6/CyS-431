import numpy as np

def ExponentVector(n, b):
    EV = np.zeros(b.size)
    if n % b[0] == 0:
        EV[0] = 1
    for i in range(1, b.size):
        if n % b[i] == 0:
            EV[i] = 1
            j = 0
            while n % b[i]**j == 0:
                j += 1
                EV[i] = j - 1
        else:
            EV[i] = 0
    return EV


if 