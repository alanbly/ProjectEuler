from collections import defaultdict


cubes = [i**3 for i in range(0,10**6)]


cubeStrings  = [''.join(sorted(list(str(i)))) for i in cubes]


cubeMap = defaultdict(list)
for i in range(0,10**6) :
  cubeMap[cubeStrings[i]].append(cubes[i])


smallest = None
for characters, values in cubeMap.items() :
  if len(values) > 4 and (not smallest or min(values) < smallest) :
    smallest = min(values)
    print smallest