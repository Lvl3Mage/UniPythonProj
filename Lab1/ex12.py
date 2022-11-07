
hours = int(input("Enter the amount of hours: "))

days = hours // 24


if(days < 1 or days > 31):
	print('Value out of range (24-744)')
else:
	price = 0
	if(days == 1):
		price = 11
	elif(days <= 5):
		price = days*5.5
	elif(days <= 14):
		price = days*5.5
	else:
		price = days*110/31

	print('The price is {0}'.format(round(price,2)))