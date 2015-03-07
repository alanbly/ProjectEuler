from Math import *

matrix = [[131, 673, 234, 103, 18],[201, 96, 342, 965, 150],[630, 803, 746, 422, 111],[537, 699, 497, 121, 956],[805, 732, 524, 37, 331]]

matrixFile = open("p081_matrix.txt");
matrix = [[int(i) for i in i.split(",")] for i in matrixFile.read().split("\n")[0:-1]]
matrix.reverse()
for i in matrix :
  i.reverse()

for i in range(1, len(matrix[0])) :
  matrix[0][i] = matrix[0][i] + matrix[0][i-1]

for i in range(1, len(matrix)) :
  matrix[i][0] = matrix[i][0] + matrix[i-1][0]
  for j in range(1, len(matrix[i])) :
    matrix[i][j] = matrix[i][j] + min(matrix[i-1][j], matrix[i][j-1])

// 427337