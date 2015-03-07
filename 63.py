count = 0
for i in range(1, 22) : ## len(str(9**22)) == 21
  count += sum([len(str(j**i)) == i for j in range(1,10)])