numbers = []
while len(numbers) < 10:
	num = int(input("Input a positive number: "))
	if(num >= 0):
		numbers.append(num)
	else:
		print("Number {0} isn't positive".format(num))

print(numbers)