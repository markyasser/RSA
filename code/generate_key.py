import random
import math

def generate_key(number_of_bits):
    p = 0
    q = 0
    start = 2**(number_of_bits//2+1)
    end = 2**((number_of_bits//2+1) + 1)
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            break
    while True:
        q = random.randint(start, end)
        if is_prime(q):
            break
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

