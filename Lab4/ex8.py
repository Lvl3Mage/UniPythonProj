from test_module import test
import math
def GetDigits(num):
	nums = []
	digitCount = math.floor(math.log10(num))+1
	for i in range(digitCount, 0,-1):
		shiftVal = num - num%(10**(i-1))
		nums.append(int(shiftVal/(10**(i-1))))
		num = num - shiftVal
	return nums

if __name__== '__main__':
	userInput = 1
	while userInput > 0:
		userInput = int(input("Enter a positive whole number (0 or negative to exit):"))
		if(userInput > 0):
			print(GetDigits(userInput))
	
