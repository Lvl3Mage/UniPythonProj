num = int(input("Input a number: "))

base = 1
powr = 1
while(powr < num):
	nextBase = base+1
	powr = nextBase**2
	if(powr <= num):
		base = nextBase

print(base)