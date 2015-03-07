def substrings(string) :
  strLen = len(string)
  for i in range(0, strLen) :
    for j in range(i+1, strLen+1)[::-1] :
      yield string[i:j]


def rangeGen(start, end) :
  cursor = start
  while cursor < end :
    yield cursor
    cursor += 1


def oneChild(n) :
  string = str(n)
  strLen = len(string)
  one = False
  for substring in substrings(string) :
    if int(substring) % strLen == 0 :
      if one : return False
      one = True
  return one

  if strLen == 10 or string.count('0')+string.count(str(strLen)) > 1 : return False

def countOnes(length, base='', divisors=[]) :
  if len(base) >= length : 


count = 0
value = 0
for i in rangeGen(1,10**19) :
  if oneChild(i) : count += 1
  if i % 10**6 == 0 : print "%d - %d" % (i, count)




