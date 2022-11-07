while True:
	#Input section
	string = input("Enter a string (empty to exit): ")
	if(string == ''): #Exit condition
		break;

	#Word counting
	words = 0
	prev = " "

	for char in string:
		if(char != " " and prev == " "):# Detects when a new word starts
			words += 1
		prev = char;

	#Output
	print("Words: {0}".format(words))