import math
def ReadMatrix(isSquare = False):
	matHeight = None
	matWidth = None
	if(not isSquare):
		matWidth = int(input("Enter the width of the matrix: "))
		matHeight = int(input("Enter the height of the matrix: "))
	else:
		matSize = int(input("Enter the size of the matrix: "))
		matHeight = matSize
		matWidth = matSize
	mat = []
	for i in range(matHeight):
		row = []
		for j in range(matWidth):
			row.append(abs(int(input("Enter the value of the cell ({0}, {1}): ".format(j, i)))))
		mat.append(row)
	return mat
def MaxNum(nums):
	maxNum = float('-inf')
	for num in nums:
		if(maxNum < num):
			maxNum = num
	return maxNum
def PrintMatrixUniform(mat):
	maxNums = []
	for row in mat:
		maxNums.append(MaxNum(row))
	maxNum = MaxNum(maxNums)
	targetWidth = len(str(maxNum))
	for row in mat:
		for val in row:
			totalSpacing = targetWidth - len(str(val))
			# #for central allignment
			# halfSpacing = math.floor(totalSpacing/2)
			# cell =' '*(halfSpacing) + str(val) + ' '*(totalSpacing-halfSpacing + 1)
			cell =str(val) + ' '*(totalSpacing + 1)
			print(cell, end='')
		print('')

if __name__== '__main__':
	cont = True
	while cont:
		PrintMatrixUniform(ReadMatrix())
		cont = input("Would you like to continue (y/n): ") == 'y'
