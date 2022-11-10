def DNILetterFromNum(dniNum): 
	indexStr = "TRWAGMYFPDXBNJZSQVHLCKE"
	return indexStr[dniNum % 23]
print(DNILetterFromNum(82657691)) #S