import math
class Vector2: # A vector2 class written by me that imitates the Vector2 class from unity
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return "({0}, {1})".format(self.x,self.y)

	def __eq__(self, other):  
		return self.x == other.x and self.y == other.y
	def	__ne__(self, other):
		return self.x != other.x and self.y != other.y

	def __add__(self, other):  
		return Vector2(self.x + other.x, self.y + other.y)
	def __sub__(self, other):
		return Vector2(self.x - other.x, self.y - other.y)
	def __mul__(self, other):
		return Vector2(self.x*other, self.y*other)
	def Length(self):
		return math.sqrt(self.x**2 + self.y**2)
	def LengthSqr(self):
		return self.x**2 + self.y**2
	def Normalized(self):
		length = self.Length()
		return Vector2(self.x/length, self.y/length)
	def PerpR(self):
		return Vector2(self.y, -self.x)
	def PerpL(self):
		return Vector2(-self.x, self.y)
	def isEqual(self, other, delta = 0):
		return (other - self).LengthSqr() <= delta**2
	def Clone(self):
		return Vector2(self.x, self.y)
	def RotateByAngle(self, angle):
		angle = math.radians(angle)
		return Vector2(self.x * math.cos(angle) - self.y*math.sin(angle),self.x * math.sin(angle) + self.y*math.cos(angle))
	@staticmethod
	def Dot(vectA, vectB):
		return vectA.x*vectB.x + vectA.y*vectB.y
	@staticmethod
	def zero():
		return Vector2(0,0)
	@staticmethod
	def up():
		return Vector2(0,1)
	@staticmethod
	def down():
		return Vector2(0,-1)
	@staticmethod
	def right():
		return Vector2(1,0)
	@staticmethod
	def left():
		return Vector2(-1,0)
