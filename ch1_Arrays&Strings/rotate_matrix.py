from copy import deepcopy
def rotated_matrix(matrix):
	'''matrix = [ [ , , ],
				  [ , , ], 
				  [ , , ] ] 
				  is list of lists'''
	'''matrix = [ [(0,0) , (0,1) , (0,2)],
	              [(1,0) , (1,1) , (1,2)],
	              [(2,0) , (2,1) , (2,2)] ]'''

 	'''rotated_ matrix = [ [(2,0)  , (1,0) , (0,0)],
             	           [(2,1)  , (1,1) , (0,1)],
             	           [(2,2)  , (1,2) , (0,2)] ]'''            


	rotated_matrix = deepcopy(matrix)
	n = len(matrix)
	row = len(matrix)
	for lst in matrix:
		for i in range(n):
			rotated_matrix[i][row - 1] = lst[i]
		row -= 1

	return rotated_matrix

matrix = [ [1 , 2 , 3],
           [4 , 5 , 6],
           [7 , 8 , 9] ]
print(rotated_matrix(matrix))
