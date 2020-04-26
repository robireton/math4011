from itertools import count
import math
PRIME_DEBUG = False

# HERE IS THE NEW STUFF BASED ON A GENERATOR FOR
# THE SEQUENCE OF PRIMES

# HERE'S A GENERATOR THAT PUTS OUT THE LIST OF PRIMES
# IT ISN'T EFFICIENT SINCE IT TESTS A NUMBER FOR PRIMENESS BY
# DIVIDING BY ALL POSSIBLE SMALLER PRIMES.

PRIMES = [2, 3, 5]


def GENERATE_PRIMES(stop_at=0):
    for p in PRIMES:
        if 0 < stop_at < p:
            return  # raises the StopIteration exception
        yield p
    if len(PRIMES) >= 1:
        start_at = 2+PRIMES[len(PRIMES)-1]
    for n in count(start_at, 2):
        if 0 < stop_at < n:
            return  # raises the StopIteration exception
        # this next line might help if some other
        # generator has expanded PRIMES since we did?
        # if n in PRIMES:yield n
        composite = False
        for p in PRIMES:
            if not n % p:
                composite = True
                break
            elif p**2 > n:
                break
        if not composite:
            PRIMES.append(n)
            yield n

# THIS FUNCTION PRODUCES THE PRIME POWER
# FACTORIZATION OF ITS ARGUMENT


def FIND_FACTORS(n):
    factors = []
    for p in GENERATE_PRIMES(math.sqrt(n)):
        # print p,n
        if n % p == 0:
            c = 0
            while n % p == 0:
                c += 1
                n = n/p
            factors.append((p, c))
        if n == 1:
            break
    if n != 1:
        factors.append((n, 1))
    return factors

# Given a number n
# find the prime power factorization
# and then produce a list of all divisors


def LIST_DIVISORS(n):
    divisors = []
    divisors.append(1)
    # factors=FIND_FACTORS(n)
    for primefactor in FIND_FACTORS(n):
        for i in range(len(divisors)):
            for k in range(primefactor[1]):
                divisors.append(divisors[i]*pow(primefactor[0], k+1))
    return divisors


def assemble_prime_power(factors):
    ans = 1
    for pf in factors:
        ans = ans*pow(pf[0], pf[1])
    return ans


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def extended_gcd(a, b):
    x = 0
    lastx = 1
    y = 1
    lasty = 0
    while b != 0:
        amodb = a % b
        quotient = (a-(amodb)) / b
        temp = b
        b = amodb
        a = temp
        temp = x
        x = lastx-quotient*x
        lastx = temp

        temp = y
        y = lasty-quotient*y
        lasty = temp
    return (lastx, lasty, a)


def lcm(a, b):
    return a*b/gcd(a, b)


def is_even(n):
    if n % 2 == 0:
        return 1
    else:
        return 0


def is_odd(n):
    return n % 2


def IS_PRIME(n):
    for p in GENERATE_PRIMES(math.sqrt(n)):
        if n % p == 0:
            return False
    return True


def phi(n):
    factors = FIND_FACTORS(n)
    ans = 1
    for f in factors:
        ans = ans*(f[0]**f[1]-f[0]**(f[1]-1))
    return ans


def mu(n):
    if n == 1:
        return 1
    factors = FIND_FACTORS(n)
    for f in factors:
        if is_even(f[1]):
            return 0
    return (-1)**len(factors)


def sumddividesn(f, n):
    s = 0
    for d in LIST_DIVISORS(n):
        s = s+f(d)
    return s


def ordermodm(a, m):
    if gcd(a, m) != 1:
        return 0
    p = a
    e = 1
    ph = phi(m)
    while(p != 1 and e <= ph):
        p = (a*p) % m
        e = e+1
    return e


def primitive_roots(m):
    ans = []
    for a in range(2, m):
        if gcd(a, m) == 1:
            if ordermodm(a, m) == phi(m):
                ans.append(a)
    return ans


if __name__ == "__main__":
    print("length of PRIMES=", len(PRIMES))
    for p in GENERATE_PRIMES(1000):
        print(p)
    print("length of PRIMES=", len(PRIMES))
    print(FIND_FACTORS(1000))
    for a in range(2, 42):
        if ordermodm(a, 43) == 42:
            print(a)
    print(primitive_roots(43))
    for e in range(1, 42):
        if gcd(e, 42) == 1:
            print(3**e % 43)
    print(sumddividesn(phi, 100))
