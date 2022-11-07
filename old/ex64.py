num = int(input('Input an integer: '))

if(num % 2 == 0):
	div = int(num / 2)
	if(div % 2 != 0):
		print('The integer given is a double of an odd integer ({0})'.format(div))
	else:
		print('The integer given is a double of an even integer ({0})'.format(div))	
else:
	print('The integer given is odd')

