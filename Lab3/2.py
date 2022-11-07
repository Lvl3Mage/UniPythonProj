string = input("Enter your sentence: ")
output = ''
prevWordEnd = 0

string += ' '

for i in range(1, len(string)):
    suffix = ''
    if(string[i] == ' ' and string[i-1] != ' '):
        if(i > 2):
            if(string[i-1] != ' ' and string[i-2] != ' '):
                suffix = string[i-2: i]
        output += string[prevWordEnd:i] + suffix
        prevWordEnd = i

    # adding a space at the end of the string is equivalent to putting this code block in
    # if(i == len(string)-1):
    #     if(string[i] != ' ' and string[i-1] != ' '):
    #         suffix = string[i-1: i+1]
    #     output += string[prevWordEnd:i+1] + suffix

print(output)