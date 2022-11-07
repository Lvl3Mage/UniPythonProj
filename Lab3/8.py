n = int(input("Enter the value of n: "))
mat = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(j-i)
    mat.append(row)
for row in mat:
    print(row)