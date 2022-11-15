def MaxStrings(strings = []):
	longestStrs = []
	longestStrLength = -1
	for string in strings:
		if(len(string) == longestStrLength):
			longestStrs.append(string)
		elif(len(string) > longestStrLength):
			longestStrLength = len(string)
			longestStrs = [string]
	return longestStrs
print(MaxStrings(["1","12","123"])) # 123
print(MaxStrings(["1234","12","123"])) # 1234
print(MaxStrings(["1","12","123", "231"])) # 123 , 231