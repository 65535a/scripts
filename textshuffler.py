#!/user/bin/env python

import sys
import random
import string
import time

word = sys.argv[1]
wordlist = list(word)
letters = []
finalstring = ""

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

for l in word:
    letters.append(random.choice(chars))

while finalstring != word:
    for x in range(len(wordlist)):
        for y in letters:
            if letters[x] != wordlist[x]:
                letters[x] = random.choice(chars)
    time.sleep(.05)
    finalstring = ''.join(letters)
    sys.stdout.write("\r" + finalstring)
    sys.stdout.flush()
