baseString = input("Enter the first string: ")
subString = input("Enter the second string: ")

isSubString = False
if(len(baseString) >= len(subString)):
    i = 0
    while (i < len(baseString)-len(subString)+1 and not isSubString):
        if(baseString[i:i+len(subString)] == subString):
            isSubString = True
        i+=1

if(isSubString):
    print("String '{0}' contains '{1}'".format(baseString,subString))
else:
    print("String '{0}' does not contain '{1}'".format(baseString,subString))