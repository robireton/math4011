import primes


def mult_inv_mod_m(a, m):
    i = int(primes.extended_gcd(a, m)[0])
    while i < 0:
        i += m
    return i


def add_inv_mod_m(b, m):
    i = b - m
    while i < 0:
        i += m
    return i


def encode1(a, b, message):
    return "".join([chr((a * ord(c) + b) % 128) for c in message])


def decode1_char(ai, bi, c):
    return chr((ord(c) + bi) * ai % 128)


def decode1(a, b, message):
    a_inverse = mult_inv_mod_m(a, 128)
    b_inverse = add_inv_mod_m(b, 128)
    return "".join([decode1_char(a_inverse, b_inverse, c) for c in message])


def analyze(message):
    counts = [0]*128

    for y in [ord(x) for x in message]:
        counts[y] = counts[y]+1

    for i in range(0, 128):
        if counts[i] > 0:
            print(i, chr(i), counts[i])

    big = [(counts[x], x, chr(x)) for x in range(0, 128)]
    big.sort(reverse=True)
    print(big[:12])


plaintext = """Animal Crossing is a social simulation video game series 
developed and published by Nintendo and created by Katsuya Eguchi. In Animal 
Crossing, the player character is a human who lives in a village inhabited by 
various anthropomorphic animals, carrying out various activities such as 
fishing, bug catching, and fossil hunting. The series is notable for its 
open-ended gameplay and extensive use of the video game console's internal 
clock and calendar to simulate real passage of time.
Since its initial release in 2001, five Animal Crossing games have been 
released worldwide, one each for the Nintendo 64/iQue Player (enhanced and 
reissued for the GameCube), Nintendo DS, Wii, Nintendo 3DS and Nintendo Switch. 
The series has been both critically and commercially successful and has sold 
over 30 million units worldwide. Three spin-off games have also been released: 
Animal Crossing: Happy Home Designer for Nintendo 3DS, Animal Crossing: Amiibo 
Festival for Wii U, and Animal Crossing: Pocket Camp for mobile devices."""

ciphertext = encode1(3, 5, plaintext)

analyze(plaintext)
analyze(ciphertext)

decode1(3, 5, ciphertext)

challenge_message = [115, 111, 54, 45, 54, 23, 2, 64, 23, 92, 45, 106, 97, 35, 54, 102, 45, 23, 2, 97, 23, 83, 111, 2, 64, 23, 121, 2, 54, 12, 23, 116, 73, 23, 59, 2, 73, 54, 123, 23, 12, 2, 83, 111, 23, 2, 83, 64, 23, 64, 54, 121, 54, 45, 106, 59, 23, 7, 116, 12, 54, 45, 64, 123, 23, 117, 111, 106, 121, 2, 97, 92, 23, 125, 54, 54, 97, 23, 116, 45, 2, 92, 2, 97, 106, 59, 59, 50, 23, 125, 45, 54, 106, 83, 111, 54, 35, 23, 125, 50, 23, 83, 111, 54, 23, 48, 45, 54, 106, 83, 116, 45, 23, 2, 97, 83, 116, 23, 106, 23, 73, 54, 12, 23, 73, 116, 45, 78, 64, 23, 116, 45, 23, 2, 97, 83, 116, 23, 116, 97, 54, 24, 23, 117, 106, 97, 35, 23, 83, 111, 106, 83, 123, 23, 12, 111, 2, 59, 64, 83, 23, 83, 111, 2, 64, 23, 7, 59, 106,
                     97, 54, 83, 23, 111, 106, 64, 23, 92, 116, 97, 54, 23, 16, 50, 16, 59, 2, 97, 92, 23, 116, 97, 23, 106, 16, 16, 116, 45, 35, 2, 97, 92, 23, 83, 116, 23, 83, 111, 54, 23, 73, 2, 31, 54, 35, 23, 59, 106, 12, 23, 116, 73, 23, 117, 92, 45, 106, 121, 2, 83, 50, 123, 23, 73, 45, 116, 78, 23, 64, 116, 23, 64, 2, 78, 7, 59, 54, 23, 106, 23, 125, 54, 92, 2, 97, 97, 2, 97, 92, 23, 54, 97, 35, 59, 54, 64, 64, 23, 73, 116, 45, 78, 64, 23, 78, 116, 64, 83, 23, 117, 125, 54, 106, 102, 83, 2, 73, 102, 59, 23, 106, 97, 35, 23, 78, 116, 64, 83, 23, 12, 116, 97, 35, 54, 45, 73, 102, 59, 23, 111, 106, 121, 54, 23, 125, 54, 54, 97, 23, 106, 97, 35, 23, 106, 45, 54, 23, 125, 54, 2, 97, 92, 23, 54, 121, 116, 59, 121, 54, 35, 33]

analyze(challenge_message)


def get_key(r, s):
    # where r is the value of space in the encoded message and s is the encoded value for "e"
    D = 101-32  # space minus "e"
    for z in range(0, 128):
        if (D * z) % 128 == 1:
            inverse = z
            break
    ainv = inverse * (r - s) % 128
    binv = inverse * (32 * s - 101 * r) % 128
    # Then decode using ainv and binv... Hopefully it works!
    return (ainv, binv)


def get_key1(s0, s1, e0, e1):
    # s0 the code for the most common character, usually 32 · space
    # s1 the corresponding code from the cipher text
    # e0 the code for the next most common character, usually 101 · e
    # e1 the corresponding code from the cipher text
    d0 = s0 - e0
    while d0 < 0:
        d0 += 128
    d1 = s1 - e1
    while d1 < 0:
        d1 += 128
    a = (d1 * mult_inv_mod_m(d0, 128)) % 128
    b = (s1 - s0 * a) % 128
    return (a, b)


def export1(a, b, message):
    return [chr((a * ord(c) + b) % 128) for c in message]


