def primeSubDivis(string) :
  return int(string[7:])  % 17 == 0 and \
         int(string[6:9]) % 13 == 0 and \
         int(string[5:8]) % 11 == 0 and \
         int(string[4:7]) % 7  == 0 and \
         int(string[3:6]) % 5  == 0 and \
         int(string[2:5]) % 3  == 0 and \
         int(string[1:4]) % 2  == 0


import itertools

divs = []
for i in itertools.permutations(range(0,10)) :
  string = ''.join([str(num) for num in i])
  if primeSubDivis(string) : divs.append(string)
