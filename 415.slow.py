def choose(n, k):
  """
  A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
  """
  if 0 <= k <= n:
    ntok = 1
    ktok = 1
    for t in xrange(1, min(k, n - k) + 1):
      ntok *= n
      ktok *= t
      n -= 1
    return ntok // ktok
  else:
    return 0


def allSets(num, minLen = 2, maxDigits=None) :
  limit = num+1
  if num < minLen : return 0
  if num == minLen : return 1
  remove = 0
  for i in rangeGen(0, minLen) :
    remove += choose(num,i)
  if maxDigits :
    repeat = 4*5**(maxDigits-1)
    total = pow(2,(num%repeat),10**(maxDigits+1))
    if not total : total = 10**(maxDigits)
    remove %= 10**maxDigits
    if not remove : remove = 10**(maxDigits-1)
    total -= remove
    if not total : return 10**(maxDigits-1)
    return total%10**maxDigits
  return 2**num - remove


def rangeGen(start, end, step = 1) :
  cursor = start
  while cursor < end :
    yield cursor
    cursor += step


def diagCount(num, numer=1, den=1) :
  total = 0
  maxLen = (num-1) // numer + 1
  maxSets = allSets(maxLen,3,8)
  smallerSets = allSets(maxLen-1,3,8)
  dups = (num-1)%numer+1
  firstLong = (maxLen-1)*den+1
  shortScale = numer*den*(4 if numer == 1 and den == 1 else 8)
  for i in rangeGen(den*2+1,firstLong,den) :
    sets = allSets((i-1)//den+1,3,8)
    total += sets*shortScale
  total += (num-firstLong-den+1)*4*(maxSets*dups+smallerSets*(numer-dups))
  if numer == 1 and den == 1 : total += 2*maxSets
  else : total += 4*maxSets*dups*den
  return total%10**8


def commonDiv(num, den, divs) :
  for i in divs[1:] :
    if not num % i : return True
  return False


def relativePrimes(num) :
  divs = divisors(num)
  for i in rangeGen(2,num) :
    if not commonDiv(i, num, divs) : yield i


def titanSets(index) :
  num = index+1
  colinear = 0
  for i in rangeGen(1,index//2+1) : # numerators
    if not i%1000 : print i
    colinear += diagCount(num,i) # diags slope=i/1
    for j in relativePrimes(i) :
      colinear += diagCount(num, i, j) # diags slope=i/j
  colinear += 2*allSets(num,3)*(num) # straights
  total = (allSets(num**2, 2, 9)-colinear%10**8)%10**8
  return total
