for i in range(1,110):
    out = ''
    if(i % 3 == 0):
        out += "Cosa"
    if(i % 5 == 0):
        out += "Losa"
    if(i % 7 == 0):
        out += "Wosa"
    if(out == ''):
        out = i
    print("{0} ".format(out), end = "")
    if(i % 11 == 0):
        print("")