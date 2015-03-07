from math import *

def variants(n, m, memo = {}) :
  print "Variants on %d_%d" % (n, m);
  if(m == 1 or m == n or n - m == 1) :
    return 1;
  if(m > n or m <= 0) :
    return 0;
  return sumVariants(n-m, m, memo);

def sumVariants(n, m, memo = {}) :
  print "Sum variants on %d_%d" % (n, m);
  if(n == 0 or m == 0) :
    return 0;
  if(n == 1 or m == 1) :
    return 1;
  if(m > n) :
    return sumVariants(n, n, memo);
  if(n in memo and m in memo[n]) :
    return memo[n][m];
  if not n in memo :
    memo[n] = {};
  memo[n][m] = variants(n, m, memo) + sumVariants(n, m-1, memo);
  return memo[n][m];

sumVariants(5, 4)
sumVariants(100, 99)