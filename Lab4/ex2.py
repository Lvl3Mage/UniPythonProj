from test_module import test

def Divisors(val):
	divs = []
	for i in range(1,val//2 + 1):
		if(val % i == 0):
			divs.append(i)
	divs.append(val)
	return divs
# –- Unit tests –-
if __name__== '__main__':
	  
	test(Divisors(1) == [1])
	test(Divisors(10) == [1, 2, 5, 10])
	test(Divisors(9) == [1, 3, 9])
	test(Divisors(10) == [1, 2, 5, 10])
	test(Divisors(30) == [1, 2, 3, 5, 6, 10, 15, 30])
	test(Divisors(35) == [1, 5, 7, 35])
	test(Divisors(49) == [1, 7, 49])

	val = 1
	while val > 0:
		val = int(input("Enter a whole number to find the divisors for (0 or negative to exit): "))
		if(val > 0):
			print(Divisors(val)) 