from math import sqrt
def arTri(a, b, c):
	s = (a+b+c)/2
	return sqrt(s * (s-a) * (s-b) * (s-c))
s = 4
print(arTri(s-1,s,s+1))
print(s)
print(a)