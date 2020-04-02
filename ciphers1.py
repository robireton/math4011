# Few words about lists
l = [1, 2, 3, 4, 5]

print(l)

print(l[3])

l[3] = 99

print(l)


for x in l:
    print(x)


l = range(0, 10)

print(l)

for x in range(0, len(l)):
    print(x, l[x])

# strings are like lists
l = "abcdef"

for x in l:
    print(x)

# we can slice them
print(l[2:4])

print(l[2:4], l[:2], l[2:])


# making new lists
l = [1, 2, 3, 4, 5]

l = [3*x for x in l]

print(l)


# TEXT TO LISTS OF NUMBERS and back

plaintext = "This is the message that we wish to send."

print("plain=", plaintext)

# We assume that the plain text includes the usual letters and punctuation marks
# Computers represent such things internally as numbers (you can google ascii codes or unicode if interested)
# For our purposes --- converting a string of text into a sequence of numbers and back
# python provides easy tools

digitizedtext = [ord(x) for x in plaintext]


print("digitized=", digitizedtext)

# To convert digitized texts back into English we use chr()

listofcharacters = [chr(x) for x in digitizedtext]

print(listofcharacters)

# And we can form a list of characters back into a message as

outputtext = "".join(listofcharacters)

print(outputtext)


# A SIMPLE SUBSTITUTION "monoalphabetic" cipher mentioned by Burton is to replace each letter with one
# that is a fixed number of places farther down the alphabet. Let's illustrate this

plaintext = "ABCDabcdef"

print("plaintext=", plaintext)

digitizedtext = [ord(x) for x in plaintext]

print("digitizedtext=", digitizedtext)


encodedtext = [(x+3) % 128 for x in digitizedtext]

print("encodedtext=", encodedtext)

ciphertext = "".join([chr(x) for x in encodedtext])

print("ciphertext=", ciphertext)

# we can combine the steps of plaintext->ciphertext in a procedure:


def encode(key, message):
    digitext = [ord(x) for x in message]
    enctext = [(x+key) % 128 for x in digitext]
    ciphtext = "".join([chr(x) for x in enctext])
    return ciphtext


print(encode(1, "abcdef"))

# We can decode with the same procedure, just using a different key
# After encoding and decoding each x becomes x+1+127 modulo 128 = x

print(encode(127, "bcdefg"))


# FREQUENCY ANALYSIS
# A weakness of this sort of single substitution procedure in which one "letter" is
# replaced by another letter is that it is possible, with a long enough message
# to figure out some of the substitions. This is because in most texts certain letters occur
# much more frequently than others. If we include "space" as a letter it is the most frequent
# letter in most every message.

# We can count how many times each of the "letters" occurs in a message pretty
# easily

sampletext = """After having spent two sessions in Edinburgh, my father perceived, or he heard 
from my sisters, that I did not like the thought of being a physician, so he proposed that I 
should become a clergyman. He was very properly vehement against my turning into an idle sporting man, 
which then seemed my probable destination. I asked for some time to consider, as from what little 
I had heard or thought on the subject I had scruples about declaring my belief in all the 
dogmas of the Church of England; though otherwise I liked the thought of being a country clergyman. 
Accordingly I read with care 'Pearson on the Creed,' and a few other books on divinity; 
and as I did not then in the least doubt the strict and literal truth of every word in the 
Bible, I soon persuaded myself that our Creed must be fully accepted."""

counts = [0]*128

for y in [ord(x) for x in sampletext]:
    counts[y] = counts[y]+1

for i in range(0, 128):
    if counts[i] > 0:
        print(i, chr(i), counts[i])

big = [(counts[x], x, chr(x)) for x in range(0, 128)]

print(big[:2])
big.sort(reverse=True)
print(big[:5])

encodekey = 23
ciphertext = encode(encodekey, sampletext)

counts = [0]*128
for y in [ord(x) for x in ciphertext]:
    counts[y] = counts[y]+1

# for i in range(0,128):
#	if counts[i]>0:
#		print(i,chr(i),counts[i])
big = [(counts[x], x, chr(x)) for x in range(0, 128)]
big.sort(reverse=True)
print("Character frequencies for ciphertext")
print(big[:5])

# so space is probably encoded as 148
# the decode key should then be

decodekey = (128+32-55) % 128

print(decodekey)

print(ciphertext)

print(encode(decodekey, ciphertext))
