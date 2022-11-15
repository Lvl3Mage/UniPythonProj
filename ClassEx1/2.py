def MaxString(strings = []):
	longestStrLength = -1
	longestStr = None
	for string in strings:
		if(len(string) > longestStrLength):
			longestStrLength = len(string)
			longestStr = string
	return longestStr
print(MaxString(["1","12","123"])) # 123
print(MaxString(["1234","12","123"])) # 1234
print(MaxString(["1","12","123", "231"])) # 123