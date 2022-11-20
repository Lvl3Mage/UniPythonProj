def Divisors(val):
	divs = []
	for i in range(1,val//2 + 1):
		if(val % i == 0):
			divs.append(i)
	divs.append(val)
	return divs
def es_perfecto(val):
	divs = Divisors(val)
	for i in range(len(divs)-1):
		val -= divs[i]
	return val == 0
print(es_perfecto(28)) # True
print(es_perfecto(8128)) # True
print(es_perfecto(123)) # False