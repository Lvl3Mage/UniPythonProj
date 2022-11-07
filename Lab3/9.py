matSize = int(input("Enter the order of the matrix: "))

mat = []
for i in range(matSize):
	row = []
	for j in range(matSize):
		row.append(int(input("Enter the value of the cell ({0}, {1}): ".format(j, i))))
	mat.append(row)

	
isTriang = True
i = 0
while(isTriang and i < len(mat)):
	j = 0
	while(isTriang and j < len(mat[i])):
		if(j >= i): #top half
			isTriang = mat[i][j] != 0
		else: # bottom half
			isTriang = mat[i][j] == 0
		j+=1
	i+=1

if(isTriang):
	print("The matrix is triangular")
else: 
	print("The matrix is not triangular")