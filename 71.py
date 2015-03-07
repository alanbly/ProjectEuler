def commonDiv(num, den) :
  for i in divisors(den)[1:] :
    if not num % i : return True
  return False


def nextFraction(num, den, max) :
  quot = float(num)/den
  maximum = 0
  maxQ = (0,0)
  for i in range(max-den,max)[::-1] :
    maxNum = i*(num+1)/den
    minNum = i*(num-1)/den
    for j in [j for j in range(minNum,maxNum)[::-1] if not commonDiv(j,i)] :
      ratio = float(j)/i
      if ratio < quot and ratio > maximum : 
        maximum = ratio
        maxQ = (j,i)
  return maxQ


nextFraction(3,7,10**6+1)

