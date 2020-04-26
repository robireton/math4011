import primes


def modular_power(b, e, m):
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


def mult_inv_mod_m(a, m):
    i = int(primes.extended_gcd(a, m)[0])
    while i < 0:
        i += m
    return i


def generate_keys(p, q):
    # given two primes, calculate modulus M
    M = p * q
    # calculate phi(M) [(p - 1)(q - 1)]
    phi = M - p - q + 1
    # obtain exponent k with gcd(k, phi(M)) == 1
    k = 1 + (M - 1) // 2
    k = k // primes.gcd(k, phi)
    # obtain multiplicative inverse of k, mod phi(M)
    l = mult_inv_mod_m(k, phi)
    return ((k, M), (l, M))


def crack_key(public):
    k, M = public
    phi = int(primes.phi(M))
    l = mult_inv_mod_m(k, phi)
    return (l, M)


def numify(message):
    return [ord(x) for x in message]


def stringify(message):
    return "".join([chr(x) for x in message])


def transform(key, message):
    e, m = key
    return [modular_power(b, e, m) for b in message]


def encrypt(key, message):
    return transform(key, numify(message))


def decrypt(key, message):
    return stringify(transform(key, message))


def test_encryption(keys, message):
    public, private = keys
    print("\ntesting encryption")
    print("public key: ", public)
    print("private key: ", private)
    print("message: ", message)
    digitext = numify(message)
    print("digitext: ", digitext)
    encrypted = transform(private, digitext)
    print("encrypted (private): ", encrypted)
    decrypted = transform(public, encrypted)
    print("decrypted: ", decrypted)
    print("roundtrip (private -> public): ", stringify(decrypted))

    encrypted = transform(public, digitext)
    print("encrypted (public): ", encrypted)
    decrypted = transform(private, encrypted)
    print("decrypted: ", decrypted)
    print("roundtrip (public -> private): ", stringify(decrypted))
