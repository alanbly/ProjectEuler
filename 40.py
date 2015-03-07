def champ(digit) :
  if digit < 10 : return digit # 1+
  if digit < 190 : # 10+
    pair = (digit+10) / 2
    if digit % 2 == 0 :
      return pair/10
    return pair%10
  if digit < 2890 : # 100+
    trip = (digit+110) / 3
    subDig = (digit-1) % 3 # == (digit+110) % 3
    if subDig == 0 :
      return trip / 100
    if subDig == 1 :
      return (trip / 10) % 10
    return trip % 10
  if digit < 38890 : # 1000+
    quad = (digit+1110) / 4
    subDig = (digit-2) % 4 # == (digit+1110) % 4
    if subDig == 0 :
      return quad / 1000
    if subDig == 1 :
      return (quad / 100) % 10
    if subDig == 2 :
      return (quad / 10) % 10
    return quad % 10
  if digit < 488890 : # 10000+
    pent = (digit+11110) / 5
    subDig = digit % 5 # == (digit+11110) % 5
    if subDig == 0 :
      return pent / 10000
    if subDig == 1 :
      return (pent / 1000) % 10
    if subDig == 2 :
      return (pent / 100) % 10
    if subDig == 3 :
      return (pent / 10) % 10
    return pent % 10
  if digit < 5888890 : # 100000+
    hex = (digit+111110) / 6
    subDig = (digit+2) % 6 # == (digit+111110) % 6
    if subDig == 0 :
      return hex / 100000
    if subDig == 1 :
      return (hex / 10000) % 10
    if subDig == 2 :
      return (hex / 1000) % 10
    if subDig == 3 :
      return (hex / 100) % 10
    if subDig == 4 :
      return (hex / 10) % 10
    return hex % 10


reduce(lambda x,y: x*y, [champ(10**i) for i in range(0, 7)])

