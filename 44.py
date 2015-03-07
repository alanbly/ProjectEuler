def pentagon(n) : return n * (3*n-1) /2


pentagons = [pentagon(i) for i in range(1,10**6)]


def isPentagon(n, mindex = 0, maxdex = -1) :
  minVal = abs(pentagons[mindex] - n)
  maxVal = abs(pentagons[maxdex] - n)
  if minVal < maxVal :
    return n in pentagons[mindex+1:maxdex]
  return n in pentagons[maxdex-1:mindex:-1]
  

for i in range(1, len(pentagons)) :
  high = pentagons[i]
  found = False
  print high
  for j in range(0,i)[::-1] :
    low = pentagons[j]
    diff = high-low
    if isPentagon(high+low, mindex = i, maxdex = i+j) and isPentagon(diff, maxdex = i, mindex = i - j) :
      print "%d - %d = %d" % (high, low, diff)
      found = True
      break
  if found : break


7042750 - 1560090 = 5482660
