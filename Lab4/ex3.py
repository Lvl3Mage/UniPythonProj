from test_module import test
from ex2 import Divisors

def areFriendly(n1,n2):
	divs1 = Divisors(n1)
	sumDivs1 = 0
	for i in range(len(divs1)-1):
		sumDivs1 += divs1[i]

	if(sumDivs1 != n2):
		return False

	divs2 = Divisors(n2)
	sumDivs2 = 0
	for i in range(len(divs2)-1):
		sumDivs2 += divs2[i]
	return sumDivs2 == n1
	# El código de la función debe ir aquí

# –- Unit tests –-
if __name__== '__main__':
	  
	test(areFriendly(30, 42) == False)
	test(areFriendly(42, 30) == False)
	test(areFriendly(220, 284) == True)
	test(areFriendly(284, 220) == True)
	test(areFriendly(2620, 2924) == True)
	test(areFriendly(6368, 6232) == True)
