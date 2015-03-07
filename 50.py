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


longest = 0
value = 0
for i in range(1,10**4)[::-1] :
  if not primeList[i] : continue
  total = i
  count = 1;
  for j in range(1,i)[::-1] :
    if not primeList[j] : continue
    total += j
    count += 1
    if total >= 10**6 : break 
    if primeList[total] and count > longest :
      print "%d %d (%d-%d)" % (count, total, j, i)
      longest = count
      value = total
