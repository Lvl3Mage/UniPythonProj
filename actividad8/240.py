n = int(input("Enter a number: "))

matrix = []
for i in range(n):
	row = []
	for j in range(n):
		row.append(1 if j == i else 0)
	matrix.append(row)