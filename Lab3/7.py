import math




num1 = abs(int(input("Enter a positive integer: ")))
nums1 = []
digitCount = math.floor(math.log10(num1))+1
for i in range(digitCount, 0,-1):
	shiftVal = num1 - num1%(10**(i-1))
	nums1.append(int(shiftVal/(10**(i-1))))
	num1 = num1 - shiftVal

num2 = abs(int(input("Enter a positive integer: ")))
nums2 = []
digitCount = math.floor(math.log10(num2))+1
for i in range(digitCount, 0,-1):
	shiftVal = num2 - num2%(10**(i-1))
	nums2.append(int(shiftVal/(10**(i-1))))
	num2 = num2 - shiftVal
sumArr = []
if(len(nums1) != len(nums2)):
	print("Numbers have a different amount of digits")
else:
	carry = 0
	for i in range(len(nums1)-1, -1, -1):
		total = nums1[i] + nums2[i] + carry
		carry = 0
		if(total > 9):
			carry = 1
			total -= 10
		sumArr.append(total)
	if(carry > 0):
		sumArr.append(carry)
	for i in range(len(sumArr)//2):
		temp = sumArr[i]
		sumArr[i] = sumArr[-i-1]
		sumArr[-i-1] = temp
	print(sumArr)