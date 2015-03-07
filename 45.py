def triangle(n) : return n * (n+1) /2


def pentagon(n) : return n * (3*n-1) /2


def hexagon(n) : return n * (2*n-1)


triangles = [triangle(i) for i in range(1,10**6)]
pentagons = [pentagon(i) for i in range(1,10**6)]
hexagons = [hexagon(i) for i in range(1,10**6)]


pentDex = 144
triDex = 144
for i in range(144, 10**6) :
  hexVal = hexagons[i]
  while pentagons[pentDex] < hexVal : pentDex += 1; triDex += 1
  while triangles[triDex] < hexVal : triDex += 1
  if hexVal == pentagons[pentDex] and hexVal == triangles[triDex] :
    print hexVal
    break

