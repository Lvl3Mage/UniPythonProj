from turtle import *
import math



radius = int(input("Enter the radius: "))
n = int(input("Enter the amount of points: "))

trt = Turtle()
trt.speed(0)

itr = 150
angleStep = math.pi*2/itr
trt.penup()
trt.goto(radius,0)
trt.pendown()
offset = 0
for i in range(itr+1):
	trt.goto(math.cos(offset + i*angleStep)*radius, math.sin(offset + i*angleStep)*radius)
trt.penup()

pointsIN = 0
for i in range(n):
	x = float(input("Enter an x coordinate: "))
	y = float(input("Enter a y coordinate: "))
	trt.goto(x,y)
	trt.dot(5)
	if(x**2+y**2 <= radius**2):
		pointsIN+=1
print("{0} points were inside the circle".format(pointsIN))
trt.hideturtle()


exitonclick()




