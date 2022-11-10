def DNILetterFromNum(dniNum): 
	indexStr = "TRWAGMYFPDXBNJZSQVHLCKE"
	return indexStr[dniNum % 23]
def DNIValid(dniNum, dniLetter):
    return DNILetterFromNum(dniNum) == dniLetter
print(DNIValid(82657691, "M")) # False
print(DNIValid(82657691, "S")) # True