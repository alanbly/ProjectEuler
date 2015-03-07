triangles = [(n*(n+1))/2 for n in range(1, 10**3)]

def wordVal(word) :
  base = ord('A') - 1
  return sum([ord(i) - base for i in list(word)])


count = 0
for word in words :
  if wordVal(word) in triangles : count += 1
