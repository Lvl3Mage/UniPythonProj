from test_module import test

def AddDigits(digits1, digits2):
	if(len(digits1) != len(digits2)):
		sumArr = None
	else:
		carry = 0
		sumArr = [0] * len(digits1)
		for i in range(len(digits1)-1, -1, -1):
			total = digits1[i] + digits2[i] + carry
			carry = 0
			if(total > 9):
				carry = 1
				total -= 10
			sumArr[i] = total
		if(carry > 0):
			sumArr = [carry] + sumArr
	return sumArr

# –- Unit tests –-
if __name__== '__main__':
	  
	test(AddDigits([3,5,4], [1,6,3]) == [5,1,7])
	test(AddDigits([9,9,9], [9,9,9]) == [1,9,9,8])
	test(AddDigits([9,9,9], [1]) == None)
	test(AddDigits([], [9,9,9]) == None)
	test(AddDigits([7,9,9,9], [2,0,0,0]) == [9,9,9,9])
	test(AddDigits([9,9,9,9], [2,0,0,0]) == [1,1,9,9,9])
