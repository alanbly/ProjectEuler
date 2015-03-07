def isPalindrome(num) :
  string = str(num)
  bottomHalf = len(string)/2
  topHalf = (len(string)-1)/2
  return string[:bottomHalf] == string[:topHalf:-1]

def lychrel(num, depth=0) :
  if depth >= 50 : return False
  added = num + int(str(num)[::-1])
  return isPalindrome(added) or lychrel(added, depth+1)


sum([lychrel(i) for i in range(1,10000)])

