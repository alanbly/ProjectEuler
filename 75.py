from math import *
from itertools import *
from divisor import *

def bruteForceTriangles(n) :
  triangles = [];
  for i in range((n)/3,n-1) :
    #print "try %d" % i;
    target = i*i;
    others = n-i;
    othersSq = others*others;
    for j in range((others+1)/2,others) :
      diff = others-j;
      #print "try [%d, %d, %d] => %f %f" % (i,j,diff,j*j + diff*diff,target);
      if j*j + diff*diff == target : # this is j^2 + (n-i-j)^2 == i^2 = j^2 + j^2 - 2 j(n-i) + (n-i)^2
        triangles.append([i,j,diff]);
  return triangles;

bruteForceTriangles(4);
bruteForceTriangles(12);
bruteForceTriangles(120);


hcf = lambda n1, n2: n1 if n2 == 0 else hcf( n2, n1 % n2 )

def coprime( n1, n2 ):
  return hcf( n1, n2 ) == 1

def euclid(m, n, k) :
  #  a = k\cdot(m^2 - n^2)   ,\ \, b = k\cdot(2mn) ,\ \, c = k\cdot(m^2 + n^2)
  m2 = m**2;
  n2 = n**2;
  return [k*(m2 - n2), 2*k*m*n, k*(m2+n2)];

def genEuclid(max) :
  for n in xrange(1,int(sqrt(max/4)) + 1) :
    for m in xrange(n+1,(int(sqrt(n**2+2*max))-n)/2+2,2) :
      #print "%d and %d are coprime ?" % (m, n)
      if(coprime(m, n)) :
        #print "%d and %d are coprime" % (m, n)
        for k in xrange (1, max/(2*m*(m+n))+1) :
          val = euclid(m,n,k);
          #print "Trying %d %d %d -> %s" % (m, n, k, str(val))
          yield val;

def buildTriangles(n, memo = {}) :
  for tri in genEuclid(n) :
    L  = sum(tri);
    print "Triangle %s at %d" % (str(tri), L)
    if L in memo :
      memo[L] += 1;
    else :
      memo[L] = 1;
  return memo;

buildTriangles(12)
buildTriangles(48)
buildTriangles(120)

def countTriangles(n, memo = {}) :
  buildTriangles(n, memo);
  return [L for L in memo if memo[L] == 1];

countTriangles(12)
countTriangles(48)
countTriangles(1500000)