def isConcat(string): # determines whether the input string could be a result of a concatenation between two identical strings
	if(len(string) % 2 != 0): # can't make an odd string with duplicate string concatenation
		return False
	return string[:int(len(string)/2)] == string[int(len(string)/2):] # check whether the first half of the string equals the second
print(isConcat("abb")) # False
print(isConcat("ababab")) # False
print(isConcat("abab")) # True
	