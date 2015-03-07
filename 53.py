def choose(n, k):
  """
  A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
  """
  if 0 <= k <= n:
    ntok = 1
    ktok = 1
    for t in xrange(1, min(k, n - k) + 1):
      ntok *= n
      ktok *= t
      n -= 1
    return ntok // ktok
  else:
    return 0


oneMil = 10**6
count = 0
for i in range(23, 101) :
  r = 1
  while choose(i, r) <= oneMil :
    r += 1
  count += i - 2*r + 1
  print "%d C %d -> %d" % (i, r, count)