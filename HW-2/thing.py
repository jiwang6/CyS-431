# Python program for the extended Euclidean algorithm
def EEA(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = EEA(b % a, a)
        return gcd, y - (b // a) * x, x
 
 
if __name__ == '__main__':
 
    gcd, x, y = EEA(30, 50)
    print('The GCD is', gcd)
    print(f'{gcd} = {x}*a + {y}*b')