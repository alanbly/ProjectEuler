import math
from collections import defaultdict
def digitFact(num) :
  return sum([math.factorial(int(i)) for i in list(str(num))])


factorials = {}
for i in range(1,2177282) : factorials[i] = digitFact(i)


paths = defaultdict(list)
for value, fact in factorials.items() : paths[fact].append(value)


distances = {169 : 3, 363601 : 3, 1454 : 3, 871: 2, 45361: 2, 872: 2, 45362: 2}
for i in range(2,60) :
  next = [j for j,k in distances.items() if j < 10**6 and k == i]
  up = i+1
  for j in next :
    for k in [k for k in paths[j] if not k in distances] :
      distances[k] = up


sum([i < 10**6 and j >= 60 for i,j in distances.items()])
