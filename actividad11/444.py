fileName = input("Enter the file name: ")
queryWord = input("Enter the word to search for: ")
queryResult = 0;
file = open(fileName, 'r')
for line in file:
	words = line.strip().split(' ')
	for word in words:
		if(word == queryWord):
			queryResult += 1
print("Word '{0}' appears {1} time{2} in file '{3}'.".format(queryWord, queryResult, '' if queryResult == 1 else 's', fileName))
file.close()