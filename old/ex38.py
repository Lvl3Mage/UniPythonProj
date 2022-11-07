import math

sides = []

while len(sides) < 3:
	side = input('input the length of the side number {0}:'.format(len(sides)+1))
	try:
		side = float(side)
	except:
		print('side must be a number')
	else:
		valid = side > 0
		if(len(sides) == 2 and valid):
			maxSideLen = sides[0] + sides[1]
			valid = side < maxSideLen
		if(valid):
			sides.append(side) #exit condition satisfaction
		else:
			print('side cannot construct a valid triangle')

	
P = 0
for side in sides:
	P += side

s = P/2

A = math.sqrt(s*(s-sides[0])*(s-sides[1])*(s-sides[2]))


print('the perimeter of your triangle is: {0} units'.format(P))
print('the area of your triangle is: {0} units squared'.format(A))