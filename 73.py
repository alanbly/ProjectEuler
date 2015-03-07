def commonDiv(num, den, divs = None) :
  if not divs : divs = divisors(den)
  for i in divs[1:] :
    if not num % i : return True
  return False


def validNums(den, minNum, maxNum) :
  divs = divisors(den)
  return [i for i in range(minNum,maxNum+1) if not commonDiv(i, den, divs)]


def countBetween(lowNum, lowDen, highNum, highDen, maxDen) :
  total = 0
  for i in range(2,maxDen+1) :
    minNum = i*lowNum/lowDen+1
    maxNum = (i*highNum-1)/highDen
    nums = validNums(i, minNum, maxNum)
    total += len(nums)
    #print "%d -> %d to %d (%s) %d" % (i, minNum, maxNum, ','.join([str(i) for i in nums]), total)
  return total


countBetween(1, 3, 1, 2, 12000)

