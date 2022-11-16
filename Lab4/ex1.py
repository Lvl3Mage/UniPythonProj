from test_module import test

def isNarcissistic (val):
    digits = str(val)
    n = len(digits)
    total = 0
    for i in range(n):
        digitPow = int(digits[i])**n
        total += digitPow
    return val == total

    # El código de la función debe ir aquí
    
# –- Unit tests –-
if __name__== '__main__':
      
    test(isNarcissistic(1) == True)
    test(isNarcissistic(153) == True)
    test(isNarcissistic(154) == False)
    test(isNarcissistic(406) == False)
    test(isNarcissistic(407) == True)
    test(isNarcissistic(8208) == True)
    test(isNarcissistic(92727) == True)
    test(isNarcissistic(548834) == True)
    test(isNarcissistic(24678051) == True)
