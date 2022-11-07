string = input("Input your verb: ")
end = string[len(string)-2:]
if(end == 'ar' or end == 'er' or end == 'ir'):
    string = string[:len(string)-2] + 'ing'
else:
    string += 'tion'
print(string)
