import math
class Vector3:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
	def __str__(self):
		return "({0}, {1}, {2})".format(self.x,self.y, self.z)

	def __eq__(self, other):  
		return self.x == other.x and self.y == other.y and self.z == other.z
	def	__ne__(self, other):
		return self.x != other.x and self.y != other.y and self.z != other.z

	def __add__(self, other):  
		return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
	def __sub__(self, other):
		return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
	def __mul__(self, other):
		return Vector3(self.x*other, self.y*other, self.z*other)
	def Length(self):
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)
	def LengthSqr(self):
		return self.x**2 + self.y**2 + self.z**2
	def Normalized(self):
		length = self.Length()
		return Vector3(self.x/length, self.y/length, self.z/length)
	def isEqual(self, other, delta = 0):
		return (other - self).LengthSqr() <= delta**2
	def Clone(self):
		return Vector3(self.x, self.y, self.z)
	@staticmethod
	def zero():
		return Vector3(0,0,0)
	@staticmethod
	def up():
		return Vector3(0,1,0)
	@staticmethod
	def down():
		return Vector3(0,-1,0)
	@staticmethod
	def right():
		return Vector3(1,0,0)
	@staticmethod
	def left():
		return Vector3(-1,0,0)
	@staticmethod
	def forward():
		return Vector3(0,0,1)
	@staticmethod
	def backward():
		return Vector3(0,0,-1)
