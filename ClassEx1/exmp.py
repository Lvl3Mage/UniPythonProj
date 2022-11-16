M = []
n = int(input("Introducir el número de filas y columnas: "))
latino = True

for i in range(n):
    M.append([0]*n)

for i in range(n):
    for j in range(n):
        M[i][j] = int(input("Componente {0},{1}: " .format(i,j)))
        if M[i][j] > n or M[i][j] <= 0:
            latino = False


#Impresión de datos
print("La matriz es:")

for i in range(n):
    for j in range(n):
        print(M[i][j], end=" ")
    print()

#Determinamos si la matriz es un cuadrado latino
filas = len(M)
column = len(M[0])
i= 0

while i < filas and latino:
    j = 0
    while j < column and latino:
        if M[i-1] == M[i]:
            latino = False
        if M[i-1][j-1] == M[i][j]:
            latino = False
        else:
            j += 1
    if latino:
        i += 1

if latino:
    print("Es un cuadrado latino")
else:
    print("No es un cuadrado latino")