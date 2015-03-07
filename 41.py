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


def isPandigital(num) :
  digits = list(str(num))
  digits.sort()
  return ''.join(digits) == ''.join([str(i) for i in range(1, len(digits)+1)])


for prime in range(13,10**7)[::-1] :
  if primeList[prime] and isPandigital(prime) : print prime; break


