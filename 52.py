def multiMatch(n) :
  digits = list(str(n))
  digits.sort()
  base = ''.join(digits)
  for i in range(2,7) :
    digits = list(str(i*n))
    digits.sort()
    if ''.join(digits) != base : return False
  return True


for i in range(5,10) :
  for j in rangeGen(10**i, 1.7*10**i) :
    if multiMatch(j) : print "%d %d %d %d %d %d" % (j, 2*j, 3*j, 4*j, 5*j, 6*j); break
