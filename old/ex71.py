char = input('Input a character: ')[0]
order = ord(char)

if(order >= 65 and order <= 90): # ord('A') & ord('Z')
	print('Letter "{0}" is a capital letter'.format(char))
elif(order >= 97 and order <= 122): # ord('a') & ord('z')
	print('Letter "{0}" is a lowercase letter'.format(char))
else:
	print("\"{0}\" isn't a letter".format(char));