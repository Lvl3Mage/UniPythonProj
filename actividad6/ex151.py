string = input("Input a string: ")

capitals = 0
for letter in string:
	if(letter.isupper()):
		capitals += 1

print("The string '{0}' contains {1} capital letters".format(string, capitals))