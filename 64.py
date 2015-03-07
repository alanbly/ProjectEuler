from bigfloat import *
import math


def nextStep(base, num, den) :
  rtBase = base**0.5
  newNum = den * -1
  newDen = (base - den**2)/num
  step = 0
  while rtBase + newNum > newDen :
    step += 1
    newNum -= newDen
  return (step, newNum, newDen)


def matchSeq(seq, val) :
  return seq.index(val) if val in seq else -1


def findRepeat(num) :
  with precision(200) :
    (frac, start) = math.modf(pow(num,0.5))
    if frac == 0 : return 0
    divis = [(1, -1*start)]
    (next, newNum, newDen) = nextStep(num, 1, -1*start)
    seqStart =  matchSeq(divis, (newDen, newNum))
    while seqStart < 0:
      divis.append((newDen, newNum))
      start = next
      (next, newNum, newDen) = nextStep(num, newDen, newNum)
      seqStart =  matchSeq(divis, (newDen, newNum))
    length = len(divis)-seqStart
    for i in range(0, length) :
      divis.append((newNum, newDen))
      start = next
      (next, newNum, newDen) = nextStep(num, newDen, newNum)
    #print "%d -> %s -> %d" % (num, ','.join([str(i) for i in divis]), length)
    return length


sum([findRepeat(i)%2 == 1 for i in range(2,10001)])
  


