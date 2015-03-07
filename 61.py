from itertools import chain
from collections import defaultdict

def square(n) : return n*n


def triangle(n) : return n * (n+1) /2


def pentagon(n) : return n * (3*n-1) /2


def hexagon(n) : return n * (2*n-1)


def heptagon(n) : return n * (5*n-3) /2


def octagon(n) : return n * (3*n-2)


squares = [i for i in [square(i) for i in range(1,10**6)] if len(str(i)) == 4]
triangles = [i for i in [triangle(i) for i in range(1,10**6)] if len(str(i)) == 4]
pentagons = [i for i in [pentagon(i) for i in range(1,10**6)] if len(str(i)) == 4]
hexagons = [i for i in [hexagon(i) for i in range(1,10**6)] if len(str(i)) == 4]
heptagons = [i for i in [heptagon(i) for i in range(1,10**6)] if len(str(i)) == 4]
octagons = [i for i in [octagon(i) for i in range(1,10**6)] if len(str(i)) == 4]


scales = {2: squares, 3: triangles, 5: pentagons, 6: hexagons, 7: heptagons, 8: octagons}
lists = defaultdict(list)
for type, scale in scales.items() :
  for i in scale : lists[i].append(type)


steps = defaultdict(list)
for key,types in lists.items() :
  end = str(key)[-2:]
  next = [j for j in lists.keys() if str(j)[:2] == end and set(lists[j]) - set(types)]
  if next : steps[key] = next


# a typo above made the desperation below possible, thank you dynamically-scoped variables
start = set(octagons)
for seq in permutations([2,3,5,6,7]) :
  for i in octagons :
    path = [i]
    next = set(steps[i])
    for j in set(scales[seq[0]]) & next :
      path2 = path+[j]
      next2 = set(steps[j])
      for k in set(scales[seq[1]]) & next2 :
        path3 = path2+[k]
        next3 = set(steps[k])
        for l in set(scales[seq[2]]) & next3 :
          path4 = path3+[l]
          next4 = set(steps[l])
          for m in set(scales[seq[3]]) & next4 :
            path5 = path4+[m]
            next5 = set(steps[m])
            #print "%s -> %s" % (','.join([str(i) for i in path5]), ','.join([str(i) for i in next5]))
            for n in set(scales[seq[4]]) & next5 :
              path6 = path5+[n]
              next6 = set(steps[n])
              if i in next6 :
                print seq
                print path6



