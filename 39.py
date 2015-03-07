def triangles(perimeter) :
  tris = []
  c = (perimeter-1)/2
  while c > 2 :
    sqr = c*c
    a = 1
    b = perimeter - (c+a)
    while a < b :
      if a*a + b*b == sqr : tris.append([a,b,c])
      a += 1
      b -= 1
    c -= 1
  return tris


longest = 0
p = 0
for i in range(12,1001) :
  tris = triangles(i)
  count = len(tris)
  if count > longest :
    longest = count
    p = i

