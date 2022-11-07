import math
num = abs(int(input("Enter a positive integer: ")))

nums = []


digitCount = math.floor(math.log10(num))+1
for i in range(digitCount, 0,-1):
	shiftVal = num - num%(10**(i-1))
	nums.append(int(shiftVal/(10**(i-1))))
	num = num - shiftVal
	
print(nums)

# shift = 1
# while num / shift > 1:
# 	shiftedVal = math.floor(num/shift)
# 	nums.append(shiftedVal - math.floor(shiftedVal/10)*10)
# 	# nums.insert(0,shiftedVal - math.floor(shiftedVal/10)*10)
# 	shift*=10
# for i in range(len(nums)//2):
# 	temp = nums[i]
# 	nums[i] = nums[-i-1]
# 	nums[-i-1] = temp