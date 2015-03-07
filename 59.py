from itertools import product
import re

cryptFile = open("cipher1.txt")
cryptText = cryptFile.read()
cryptFile.close()

cryptInts = [int(i) for i in cryptText[:-1].split(",")]

wordFile = open("words.txt")
wordText = wordFile.read()
wordFile.close()

words = [i.lower() for i in re.split('"[,"]*', wordText[:-1])]


code = None
most = 0
for first in 'qwertyuiopasdfghjklzxcvbnm' :
  key = first+"od"
  decrypt = ""
  limit = 40#len(cryptInts)
  for i in range(0, limit)[::3] :
    for j in range(0, 3) :
      if i+j >= limit : break
      decrypt += chr(cryptInts[i+j]^ord(key[j]))
  count = sum([len(re.findall(word, decrypt, re.I)) for word in words])
  if count > most :
    most = count
    code = key
    print "%s %s" % (decrypt, key)


decrypt = ""
key = "god"
limit = len(cryptInts)
for i in range(0, limit)[::3] :
  for j in range(0, 3) :
    if i+j >= limit : break
    decrypt += chr(cryptInts[i+j]^ord(key[j]))


sum([ord(i) for i in decrypt])
