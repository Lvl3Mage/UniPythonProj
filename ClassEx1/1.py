def isApoc(val):
	sq = 2**val
	string = str(sq)
	if(len(string) <3):
		return False
	for i in range(len(string)-2):
		if(string[i] == "6" and string[i+1] == "6" and string[i+2] == "6"):
			return True
	return False
print(isApoc(157)) #True
print(isApoc(120)) #False