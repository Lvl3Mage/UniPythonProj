n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

num = n;
print("Multiples of {0} between {0} and {1}: ".format(n,m), end='')
while num < m:
	num+=1
	if(num % n == 0):
		if(num != m):
			print(num, end=', ')
		else:
			print(num)
		