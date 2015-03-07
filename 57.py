overBal = 0
expansion = 2
prevDen = 2
den = 5
prevNum = 3
num = 7
while expansion < 1000 :
  nextDen = 2*den + prevDen
  nextNum = 2*num + prevNum
  expansion += 1
  if len(str(nextDen)) < len(str(nextNum)) :
    overBal += 1
  prevDen = den
  den = nextDen
  prevNum = num
  num = nextNum


print overBal
