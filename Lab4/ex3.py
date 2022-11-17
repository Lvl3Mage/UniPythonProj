from test_module import test
from ex2 import Divisors
def ListSum(nums):
	total = 0
	for num in nums:
		total += num
	return total
def areFriendly(n1,n2):
	divs1 = Divisors(n1)
	sumDivs1 = ListSum(divs1[:-1])
	friendly = sumDivs1 == n2
	if(friendly):
		divs2 = Divisors(n2)
		sumDivs2 = ListSum(divs2[:-1])
		friendly = sumDivs2 == n1
	return friendly

# –- Unit tests –-
if __name__== '__main__':
	  
	test(areFriendly(30, 42) == False)
	test(areFriendly(42, 30) == False)
	test(areFriendly(220, 284) == True)
	test(areFriendly(284, 220) == True)
	test(areFriendly(2620, 2924) == True)
	test(areFriendly(6368, 6232) == True)
