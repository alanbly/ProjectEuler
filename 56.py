def digitSum(num) :
  value = num
  total = 0
  while value > 0 :
    total += value % 10
    value /= 10
  return total


maxSum = 0
for i in range(1,100) :
  for j in range(1,100) :
    value = digitSum(i**j)
    if value > maxSum :
      maxSum = value


print maxSum
