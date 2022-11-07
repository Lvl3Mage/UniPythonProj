from turtle import *
import math


trt = Turtle()
trt.speed(0)
trt.color('black')
side = float(input("Enter the side length: "))


x = -side/2
y = -side/2
trt.penup()
trt.goto(x,y)
trt.pendown()
trt.goto(x, y + side)
trt.goto(x + side, y + side)
trt.goto(x + side, y)
trt.goto(x, y)
trt.penup()


x = 0
y = 0
itr = 20
radius = side/2

angleStep = math.pi*2/itr
trt.penup()
trt.goto(radius + x,0)
trt.pendown()
offset = 0
for i in range(itr+1):
	trt.goto(math.cos(offset + i*angleStep)*radius + x, math.sin(offset + i*angleStep)*radius + y)
trt.penup()

exitonclick()