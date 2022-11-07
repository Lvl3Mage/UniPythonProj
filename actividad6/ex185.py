# I'm using he unidecode module to convert all the weird letters with accents to basic ASCII
# The code will run perfectly fine without it but 
# you'd need to add the weird vowels with accents to the hashmap
from unidecode import unidecode

vowels = {'a','e','i','o','u'}

inputText = unidecode(input("Input your text here: "))
outputText = ''
for char in inputText:
	if(char.lower() in vowels):
		outputText += '.'
	else:
		outputText += char
print("Output text: {0}".format(outputText));