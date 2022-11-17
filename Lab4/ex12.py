from ex11 import isLatinSquare
def CheckSudokuSquare(mat, coorX, coorY):
	foundDigits = []
	validSum = True
	i=0
	while i < 3 and validSum:
		j = 0
		while j < 3 and validSum:
			val = mat[i+coorY][j+coorX]
			validSum = val not in foundDigits
			foundDigits.append(val)
			j+=1
		i+=1
	return validSum
def isSudoku(mat):
	valid= True
	i = 0
	while i < len(mat) and valid:
		j = 0
		while j < len(mat[i]) and valid:
			valid = CheckSudokuSquare(mat, j, i) 
			j+=3
		i+=3
	if valid:
		valid = isLatinSquare(mat)
	return valid
if __name__ == '__main__':
	sudoku = [
		[5,3,4,6,7,8,9,1,2],
		[6,7,2,1,9,5,3,4,8],
		[1,9,8,3,4,2,5,6,7],
		[8,5,9,7,6,1,4,2,3],
		[4,2,6,8,5,3,7,9,1], 
		[7,1,3,9,2,4,8,5,6],
		[9,6,1,5,3,7,2,8,4],
		[2,8,7,4,1,9,6,3,5],
		[3,4,5,2,8,6,1,7,9]
	]
	print(isSudoku(sudoku))
