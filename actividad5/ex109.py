num = 0
while True:
	num = int(input("Enter a number between 0 and 10: "))
	if(num >= 0 and num <= 10):
		break
	else:
		print("{0} is not between 0 and 10".format(num))