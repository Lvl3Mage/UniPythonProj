matSize = int(input("Enter the order of the matrix: "))

mat = []
for i in range(matSize):
	row = []
	for j in range(matSize):
		row.append(int(input("Enter the value of the cell ({0}, {1}): ".format(j, i))))
	mat.append(row)

itr = 0
isLat = True
idY = 0
while(idY < len(mat) and isLat):
	idX = 0
	while(idX < len(mat[idY]) and isLat):
		val = mat[idY][idX]
		isLat = val > 0 and val <= len(mat)
		i = 0
		while(i < len(mat[idY]) and isLat):
			if(i != idX):
				isLat = mat[idY][i] != val
			i+=1
		
		i = 0
		while(i < len(mat) and isLat):
			if(i != idY):
				isLat = mat[i][idX] != val
			i+=1
		
		idX += 1
	idY +=1
print(itr)
if(isLat):
	print("The matrix is a latin square")
else: 
	print("The matrix is not a latin square")