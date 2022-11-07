l = [1,2,-5,-5,5,-6]
length = len(l)
for i in range(length):
	print(i)
	if(l[i]< 0):
		l.pop(i)
		length = len(l)
print(l)