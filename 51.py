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

def miller_rabin_isprime(a, i, n):
  """
  Miller-Rabin primality test
  returns a 1 if n is a prime
  usually i = n - 1 see
  http://en.wikipedia.org/wiki/MillerâRabin_primality_test#Deterministic_variants_of_the_test
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

def genMasks(n) :
  if n == 1 : return {1: [[0]]}
  submask = genMasks(n-1)
  submask[n] = submask[n-1]+[[n-1]]+[i+[n-1] for i in submask[n-1]]
  return submask


masks = genMasks(7)


def countMask(base, mask) :
  count = 0
  minVal = 0 if not 0 in mask else 1
  for i in range(minVal,10) :
    copy = list(base)
    for j in mask :
      copy[j] = str(i)
    if isPrime(int(''.join(copy))) : count += 1; print ''.join(copy)
  return count


def checkMasks(n, maskList) :
  base = str(n)
  longest = 0
  for mask in maskList :
    print mask
    count = countMask(base, mask)
    longest = max(count, longest)
  return longest


for i in range(10**5, 10**7) :
  if i % 100000 == 0 : print i
  if isPrime(i) :
    maskList = masks[len(str(i))]
    count = checkMasks(i, maskList)
    if count >= 8 :
      print "%d %d" % (i, count) 
      break


120383
[0, 2, 4]
121313
222323
323333
424343
525353
626363
828383
929393