convergents = [2]
for i in [[1,i*2,1] for i in range(1,34)] :
  convergents += i


def collapse(converge, num = 0, den = 1) :
  if not converge : return (den, num)
  base = converge[-1]
  return collapse(converge[:-1], den, base * den + num)


sum([int(i) for i in list(str(collapse(convergents)[0]))])
