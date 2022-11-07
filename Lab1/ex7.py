from turtle import *
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
			trt.write("({0}, {1})".format(self.x, self.y))
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
    coords.append(Coord(x, y + sideLength))
    coords.append(Coord(x + sideLength, y + sideLength))
    coords.append(Coord(x + sideLength, y))
    coords.append(Coord(x, y, True, True))
    return coords
		

trt = Turtle()
trt.speed(0)
trt.color('black')
side = float(input('Enter side length: '))

coords = [
    Coord(0, 0),
    Coord(side,side),
    Coord(side/2, side * 1.5),
    Coord(0, side),
    Coord(side, 0, True),
]
DrawCoords(trt, SquareCoords(0, 0, side,coords))

exitonclick()



