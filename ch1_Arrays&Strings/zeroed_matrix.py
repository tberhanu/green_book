#This code has some BUGS
from copy import deepcopy
def zeroed_matrix(matrix):
	zeroed_matrix = deepcopy(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				for x in range(len(matrix)):
					zeroed_matrix[x][j] = 0
				for y in range(len(matrix[0])):
					zeroed_matrix[i][y] = 0


	return zeroed_matrix

matrix1 = [ [1 , 2 , 3],
            [4 , 0 , 6],
            [7 , 8 , 9] ]
print(matrix1)
print(zeroed_matrix(matrix1))
matrix2 = [ [1 , 2 , 3],
            [4 , 0 , 6],
            [0 , 8 , 9] ]
print(zeroed_matrix(matrix2))
matrix3 = [ [0 , 2 , 3],
            [4 , 0 , 6],
            [7 , 8 , 0] ]
print(zeroed_matrix(matrix3))