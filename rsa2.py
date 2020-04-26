import primes


def modular_power(b, e, m):
    # calculate b**e %m in O(log(e)) time
    # write e in base 2
    ans = 1
    factor = b
    L = []
    while e > 0:
        if e % 2:
            L.append(1)
            e = (e-1)//2
        else:
            L.append(0)
            e = e//2

    for x in L:
        if x == 1:
            ans = (ans * factor) % m
        factor = factor*factor % m
    return ans


print(modular_power(7, 3, 128), 7**3 % 128)

# pick two primes, calculate modulus M
# and phi(M)
# IN PRACTICE, find primes between 10^N and 10^M
P1 = 23
P2 = 91
M = P1*P2
x = P1-1
y = P2-1
print(P1, P2, x, y)

PHI = M-P1-P2+1  # not (p1-1)*(p2-1)

# obtain exponent k with gcd(k,phi(M))=1
k = 1 + (M-1)//2
k = k//primes.gcd(k, PHI)


# PUBLIC KEY is (k,M)

print("P1=", P1, "P2=", P2, "M=", M, "phi(M)=", PHI, "K=", k)

plaintext = "Test message"
digitext = [ord(x) for x in plaintext]
ciphertext = [modular_power(x, k, M) for x in digitext]
print(plaintext)
print(digitext)
print(ciphertext)

# calculate decode key
ans = primes.extended_gcd(k, PHI)
print(ans)
# decoding exponent is l
l = ans[0] % PHI

# show we have the inverse
print(k*l % PHI)

print(l)
# DECODE KEY IS (l,M)
decryptedtext = [modular_power(x, l, M) for x in ciphertext]

print(decryptedtext)
print("".join([chr(x) for x in decryptedtext]))
