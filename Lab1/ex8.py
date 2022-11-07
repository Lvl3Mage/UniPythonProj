from turtle import *
import math
class Coord:
	x = 0
	y = 0
	endPath = False
	debugCoords = False
	def __init__(self,x,y, endPath = False, debugCoords = False):
		self.x = x
		self.y = y
		self.endPath = endPath
		self.debugCoords = debugCoords
	def Goto(self, trt):
		trt.goto(self.x, self.y)
		if(self.debugCoords):
			trt.write("({0}, {1})".format(round(self.x,2), round(self.y,2)))
		if(self.endPath):
			trt.penup()
		else:
			trt.pendown()

def DrawCoords(trt, coords):
	trt.penup()
	for coord in coords:
		coord.Goto(trt)
def SquareCoords(x, y, sideLength, coords = []):
	coords.append(Coord(x, y))
	coords.append(Coord(x, y + sideLength, False, True))
	coords.append(Coord(x + sideLength, y + sideLength, False, True))
	coords.append(Coord(x + sideLength, y, False, True))
	coords.append(Coord(x, y, True, True))
	return coords
def CircleCoords(x, y, radius, itr, coords = []):
	angleStep = math.pi*2/itr
	# side = math.sin(math.radians(angleStep/2))*radius*2
	offset = 0
	for i in range(itr+1):
		coords.append(Coord(math.cos(offset + i*angleStep)*radius + x, math.sin(offset + i*angleStep)*radius + y))
	coords[len(coords)-1].endPath = True
	coords[len(coords)-1].debugCoords = True
	return coords

trt = Turtle()
trt.speed(0)
trt.color('black')
x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))
radius = float(input("Enter the radius: "))

coords = [
	Coord(x, y, False, True)
]
DrawCoords(trt, CircleCoords(x, y, radius, 15, coords))

exitonclick()