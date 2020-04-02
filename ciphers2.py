# we can combine the steps of plaintext->ciphertext in a procedure:


def encode(key, message):
    digitext = [ord(x) for x in message]
    enctext = [(x+key) % 128 for x in digitext]
    ciphtext = "".join([chr(x) for x in enctext])
    return ciphtext


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

# counts=[0]*128

# for y in [ord(x) for x in sampletext]:
# 	counts[y]=counts[y]+1

# for i in range(0,128):
# 	if counts[i]>0:
# 		print(i,chr(i),counts[i])

print(sampletext)
encodekey = 23
ciphertext = encode(encodekey, sampletext)

print(ciphertext)

counts = [0]*128

for y in [ord(x) for x in ciphertext]:
    counts[y] = counts[y]+1

for i in range(0, 128):
    if counts[i] > 0:
        print(i, chr(i), counts[i])

# so space is probably encoded as 55
# the decode key should then be
# 32+k=55
# k=55-32
# decodekey=128-k

decodekey = 128-(55-32)

print(decodekey)

print(ciphertext)

print(encode(decodekey, ciphertext))
