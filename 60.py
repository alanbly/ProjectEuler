def primes(n):
  # all even numbers greater than 2 are not prime.
  s = [False]*2 + [True]*2 + [False,True]*((n-4)//2) + [False]*(n%2)
  i = 3;
  limit = n**0.5
  while i < limit:
    sq = i*i
    # get rid of ** and skip even numbers.
    s[sq : n : i*2] = [False]*(1+(n-sq)//(i*2))
    i += 2
    # skip non-primes
    while not s[i]: i += 2
  return s


primeList=primes(10**6)


primeSeq = [i for i in range(1,10**3) if primeList[i]]


def miller_rabin_isprime(a, i, n):
  """
  Miller-Rabin primality test
  returns a 1 if n is a prime
  usually i = n - 1 see
  http://en.wikipedia.org/wiki/Miller–Rabin_primality_test#Deterministic_variants_of_the_test
  for a values
  """
  if i == 0:
    return 1
  x = miller_rabin_isprime(a, i // 2, n)
  if x == 0:
    return 0
  y = (x * x) % n
  if ((y == 1) and (x != 1) and (x != (n - 1))):
    return 0
  if (i % 2) != 0:
    y = (a * y) % n
  return y


def isPrime(n) :
  if n < 10**6 : return primeList[n]
  for i in [2, 7, 61] :
    if miller_rabin_isprime(i, n-1, n) != 1 :
      return False
  return True


def arePrime(values) :
  for i in combinations(values, 2) :
    iStr = str(i[0])
    jStr = str(i[1])
    if len(iStr) + len(jStr) > 8 : return False
    if not isPrime(int(iStr+jStr)) or not isPrime(int(jStr+iStr)) :
      return False
  return True


longPairs = {}
for i in range(0, len(primeSeq))[::-1] :
  iVal = primeSeq[i]
  pairs = []
  for j in [primeSeq[i] for i in range(0, i)[::-1]] :
    iStr = str(iVal)
    jStr = str(j)
    if len(iStr) + len(jStr) > 8 : break
    if arePrime([iVal, j]) :
      pairs.append(j)
  if len(pairs) > 0 :
    longPairs[iVal] = pairs


trips = []
for val, pairs in longPairs.items() :
  for i in combinations(pairs,2) :
    if arePrime(i) :
      trips.append([val]+list(i))


quads = []
for val, pairs in longPairs.items() :
  for i in combinations(pairs,3) :
    if arePrime(i) :
      quads.append([val]+list(i))


pents = []
for i in quads :
  for j in [i+[j] for j in longPairs[i[0]]] :
    if j[-1] not in i and arePrime(j) :
      pents.append(j)
      print "%s %d" % (','.join([str(k) for k in j]), sum(j))


[8389,6733,5701,5197,13] 26033

