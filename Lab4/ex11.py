from test_module import test

def isLatinSquare(mat):
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

# –- Unit tests –-
if __name__== '__main__':
    matriz2=[[1,2,3], \
             [2,3,1], \
             [3,1,2]]
    matriz3=[[1,2,3,4], \
             [2,1,4,3], \
             [3,4,1,2], \
             [4,3,2,1]]
    matriz4=[[1,2,3,4], \
             [3,4,1,2], \
             [4,3,2,1], \
             [2,1,4,3]]
    matriz5=[[1,2,3], \
             [0,3,1], \
             [3,1,2]]
    matriz6=[[1,2,3], \
             [2,3,4], \
             [3,1,2]]
    matriz7=[[1,2,3], \
             [2,3,1], \
             [1,2,3]]
    matriz8=[[1,2,3,4], \
             [2,1,4,3], \
             [3,4,1,2], \
             [1,3,2,4]]

    test(isLatinSquare(matriz2) == True)
    test(isLatinSquare(matriz3) == True)
    test(isLatinSquare(matriz4) == True)
    test(isLatinSquare(matriz5) == False)
    test(isLatinSquare(matriz6) == False)
    test(isLatinSquare(matriz7) == False)
    test(isLatinSquare(matriz8) == False)
