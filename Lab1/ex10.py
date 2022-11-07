from turtle import *
import math

trt = Turtle()
trt.speed(0)

side = float(input("Enter the side length: "))
pointX = float(input("Enter the x coordinate: "))
pointY = float(input("Enter the x coordinate: "))

trt.color('red')
halfSide = side/2
x = -halfSide
y = -halfSide
trt.penup()
trt.goto(x,y)
trt.pendown()
trt.goto(x, y + side)
trt.goto(x + side, y + side)
trt.goto(x + side, y)
trt.goto(x, y)
trt.penup()

trt.color('blue')
x = 0
y = 0
itr = 20
radius = halfSide * math.sqrt(2)

angleStep = math.pi*2/itr
trt.penup()
trt.goto(radius + x,0)
trt.pendown()
offset = 0
for i in range(itr+1):
	trt.goto(math.cos(offset + i*angleStep)*radius + x, math.sin(offset + i*angleStep)*radius + y)
trt.penup()

trt.goto(pointX,pointY)

boundsX = pointX <= halfSide and pointX >= -halfSide;
boundsY = pointY <= halfSide and pointY >= -halfSide;

distSqr = pointX**2 + pointY**2

circleBounds = distSqr <= radius**2

clr = 'black'

if(circleBounds):
    if(boundsX and boundsY):
        clr = 'red'
    else:
        clr = 'blue'
else:
    clr = 'green'

trt.dot(5,clr)
trt.hideturtle()


exitonclick()