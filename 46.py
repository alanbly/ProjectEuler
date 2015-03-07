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


listPrimes = primes(10**6)


def isSquare(n) : return int(math.sqrt(n))**2 == n


for i in range(3, 10**6) :
  if i%2 == 1 and not listPrimes[i] :
    found = False
    for j in range(0,i)[::-1] :
      if listPrimes[j] and isSquare((i-j)/2) :
        found = True
        break
    if not found :
      print i
      break

