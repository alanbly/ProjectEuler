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


def isPermutation(a,b,c) :
  aStr = list(str(a))
  aStr.sort()
  aStr = ''.join(aStr)
  bStr = list(str(b))
  bStr.sort()
  bStr = ''.join(bStr)
  if bStr != aStr : return False
  cStr = list(str(c))
  cStr.sort()
  cStr = ''.join(cStr)
  if cStr != aStr : return False
  return True
  

for i in range(1488,10000) :
  if primeList[i] :
    found = False
    for j in range(i+1,10000) :
      next = 2*j-i
      if primeList[j] and primeList[next] and isPermutation(i,j,next) :
        print "%d%d%d" % (i,j, next)
        found = True
        break
    if found : break