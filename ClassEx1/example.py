import random
def LucasTest(M):
	filas = len(M)
	column = len(M[0])
	i= 0
	latino = True
	while i < filas and latino:
		j = 0
		while j < column and latino:
			# if M[i][j] > len(M) or M[i][j] <= 0:
			# 	latino = False
			if M[i-1] == M[i]:
				latino = False
			if M[i-1][j-1] == M[i][j]:
				latino = False
			else:
				j += 1
		if latino:
			i += 1
	return latino

def TestKarl(mat):
	isLat = True
	idY = 0
	while(idY < len(mat) and isLat):
		idX = 0
		while(idX < len(mat[idY]) and isLat):
			# for every element in the matrix
			val = mat[idY][idX]
			isLat = val > 0 and val <= len(mat)
			i = idX+1

			#check elements to the right in the current row for identical values
			while(i < len(mat[idY]) and isLat):
				isLat = mat[idY][i] != val
				i+=1
			
			i = idY+1
			#check elements below in thr current column for identical values
			while(i < len(mat) and isLat):
				isLat = mat[i][idX] != val
				i+=1
			
			idX += 1
		idY +=1
	return isLat
def CloneMat(mat):
	copyMat = []
	for i in range(len(mat)):
		row = []
		for j in range(len(mat[0])):
			row.append(mat[i][j])
		copyMat.append(row)
	return copyMat;
# print(LucasTest([[1, 3, 4, 4], [4, 3, 1, 2], [3, 2, 1, 2], [1, 1, 3, 4]]))
# print(TestKarl([[1, 3, 4, 4], [4, 3, 1, 2], [3, 2, 1, 2], [1, 1, 3, 4]]))
wrongMats = []
testMat = []
n = 3
for j in range(n):
	row = []
	for k in range(n):
		row.append(0)
	testMat.append(row)
i = 0
while i < 1000:
	for j in range(n):
		for k in range(n):
			testMat[j][k] = random.randint(1,n)
	if(TestKarl(CloneMat(testMat))):
		if(not LucasTest(CloneMat(testMat))):
			wrongMats.append((CloneMat(testMat),LucasTest(CloneMat(testMat)),TestKarl(CloneMat(testMat))))
		i+=1

for val in wrongMats:
	mat = val[0]
	print(val[1], val[2])
	for i in range(len(mat)):
		print(mat[i])
print("The error percentage is: {0}".format((len(wrongMats)/100)*100))
	