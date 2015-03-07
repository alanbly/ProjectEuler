def primefactors(n):
    i = 2
    while i<=sqrt(n):
        if n%i==0:
            l = primefactors(n//i)
            l.append(i)
            return l
        i+=1
    return [n]


three = 0
two = 0
one = 0
for i in range(2, 10**6) :
  curr = len(set(primefactors(i)))
  if three >= 4 and two >= 4 and one >= 4 and curr >= 4 :
    print "%d-%d" % (i-3,i)
    break
  three = two
  two = one
  one = curr
  if i%10**4 == 0 :
    print i

