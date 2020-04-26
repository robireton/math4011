import primes  # for extended_gcd(a,b)


plaintext = """There is grandure in this veiw of life..."""

print("plaintext", plaintext)

# We'll encode with f(x)=(ax+b)% 128 where a is chosen so that f has an inverse.
# That is, we need gcd(a,128)=gcd(a,2^7)=1. Any odd a will work

# HERE IS MY ENCODING KEY
a = 71
b = 12
encodekey = (a, b)

print("encode key", encodekey)

# CALCULATE DECODING KEY
# y=ax+b says x = a^{-1}y -a^{-1}b
# YOU FIGURE OUT HOW TO DO THIS

decodekey = (119, 108)
print("decode key", decodekey)


# ENCODE A SINGLE DIGIT USING KEY
def encode_digit(key, x):
    return (key[0]*x+key[1]) % 128

# ENCODE A LIST OF DIGITS USING KEY


def encode(key, digit_list):
    encdigits = [encode_digit(key, x) for x in digit_list]
    return encdigits

# CONVERT PLAIN TEXT TO LIST OF DIGITS
digitext = [ord(x) for x in plaintext]
print("digitized text", digitext)


# ENCODE LIST OF DIGITS WITH ENCODING KEY
encdigits = encode(encodekey, digitext)

# THIS IS THE ENCODED MESSAGE WE'LL SHARE:
print("enoded digits, message to share", encdigits)

# ENCODE THE ENCODED DIGIT LIST WITH DECODE KEY
decdigits = encode(decodekey, encdigits)

print("decoded digits", decdigits)

# CONVERT BACK TO CHARACTERS
dectext = [chr(x) for x in decdigits]

print("decoded as characters", dectext)

# AND JOIN THEM TOGETHER INTO THE ORIGINAL STRING
print("joined as a string", "".join(dectext))
