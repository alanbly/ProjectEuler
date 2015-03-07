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


def convergents(num) :
  with precision(200) :
    (frac, start) = math.modf(pow(num,0.5))
    yield math.trunc(start)
    divis = [(1, -1*start)]
    (next, newNum, newDen) = nextStep(num, 1, -1*start)
    yield next
    verge = [next]
    seqStart =  matchSeq(divis, (newDen, newNum))
    while seqStart < 0:
      divis.append((newDen, newNum))
      (next, newNum, newDen) = nextStep(num, newDen, newNum)
      yield next
      verge.append(next)
      seqStart =  matchSeq(divis, (newDen, newNum))
    length = len(divis)-seqStart
    verge = verge[-1*length:]
    while True :
      for term in verge : yield term


def collapse(converge) :
  left = converge[:]
  base = left[-1]
  left = left[:-1]
  newNum = 1
  newDen = base
  if not left : return (newNum, newDen)
  while left :
    base = left[-1]
    oldDen = newDen
    newDen = base * oldDen + newNum
    newNum = oldDen
    left = left[:-1]
  return (newDen, newNum)


def minX(d) :
  longest = 0
  gents = []
  for i in convergents(d) :
    gents.append(i)
    (x, y) = collapse(gents)
    value = x**2 - d*y**2
    if value == 1 : return x


largest = 0
maxD = 0
for d in [d for d in range(1,1001) if not isSquare(d, d**0.5)] :
  x = minX(d)
  if not d % 10 : print d
  if x and x > largest :
    largest = x
    maxD = d
    print "%d -> %d" % (d, x)
