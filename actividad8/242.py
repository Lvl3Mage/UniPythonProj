matSize = int(input("Enter the order of the matrix: "))

mat = []
for i in range(matSize):
	row = []
	for j in range(matSize):
		row.append(int(input("Enter the value of the cell ({0}, {1}): ".format(j, i))))
	mat.append(row)

mult = int(input("Enter the number to multiply the matrix by: "))


#Multiplication
for i in range(len(mat)):
	for j in range(len(mat[i])):
		mat[i][j] *= mult

print("The result of the multiplication is:")
#Result
for i in range(len(mat)):
	print(mat[i])