def SplitBy(stringToSplit, splitChar):
	splitValues = []

	lastValue = '' # contains latest value after split

	for char in stringToSplit:
		if(char == splitChar):
			splitValues.append(lastValue)
			lastValue = ''
		else:
			lastValue += char

	if(lastValue != ''):
		splitValues.append(lastValue)

	return splitValues

def AddSuffix(values, suffix):
	newValues = []
	for value in values:
		newValues.append(value + suffix)
	return newValues
def AddSuffixes(values, suffixes):
	newValues = []
	for suffix in suffixes:
		newValues += AddSuffix(values, suffix)
	return newValues

def ExpandExpression(expression):
	variations = ['']
	accValue = ''

	for char in expression:
		if(char == "{"):
			variations = AddSuffix(variations, accValue)
			accValue = ''
		elif(char == "}"):
			suffixes = SplitBy(accValue, ",")
			variations = AddSuffixes(variations, suffixes)
			accValue = ''
		else:
			accValue += char
	if(accValue != ''):
		variations = AddSuffix(variations, accValue)
	return variations

print(ExpandExpression("abc{1,2,3}abc{1,2,3}abc"))