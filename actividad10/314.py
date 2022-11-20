def QueryFirstLetter(strings, queryLetter):
	resultStrings = []
	for string in strings:
		if(string[0] == queryLetter):
			resultStrings.append(string)
	return resultStrings
print(QueryFirstLetter(["abc", "ab", "bc", "cda"], "a")) # ['abc', 'ab']