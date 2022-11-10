def Avarage(nums):
	avrg = 0
	for num in nums:
		avrg += num
	if(len(nums) > 0):
		avrg /= len(nums)
	return avrg
print(Avarage([])) #0
print(Avarage([0,2,10,5,-1])) #3.1