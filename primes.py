from math import *

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

primeList=primes(10**8)
primeSeq = [i for i in range(10**8) if primeList[i]]

def primefactors(n):
  i = 2
  while i<=sqrt(n):
    if n%i==0:
      l = primefactors(n//i)
      l.append(i)
      return l
    i+=1
  return [n]

def miller_rabin_isprime(a, i, n):
  """
  Miller-Rabin primality test
  returns a 1 if n is a prime
  usually i = n - 1
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


def phi(num, phis = {}) :
  if num == 1 : return 1
  if num in phis : return phis[num]
  if isPrime(num) :
    phis[num] = num-1
    return num-1
  product = num
  for factor in set(primefactors(num)) :
    product *= (1-1.0/factor)
  return trunc(product)
