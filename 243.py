from math import *
from divisor import *
from primes import *

def commonDiv(num, den, divs) :
  for i in divs[1:] :
    if not num % i : return True
  return False

def relativePrimes(num, divList = {}) :
  if num not in divList :
    divList[num] = divisors(num)
  relPrimes = [1]
  for i in range(2,num) :
    if not commonDiv(i, num, divList[num]) : 
      relPrimes.append(i)
  return relPrimes

relativePrimes(12)

def rangeGen(start, end = False, step = 1) :
  cursor = start
  while not end or cursor < end :
    yield cursor
    cursor += step

def findResilience(num, denom, memo = {}) :
  target = float(num)/denom
  for i in rangeGen(denom) :
    resilience = float(phi(i,memo)) / (i-1)
    if resilience < target :
      return i
    if not i % 10000 :
      print "%d -> %f (%f)" % (i, resilience, resilience-target)

findResilience(2, 5)
findResilience(15499, 94744)
