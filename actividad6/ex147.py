indexStr = "TRWAGMYFPDXBNJZSQVHLCKE"
dni = int(input("Enter your DNI without any letters: "))
print("The letter at the end of your DNI is {0}".format(indexStr[dni % 23]))