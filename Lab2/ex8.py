import random
import math
from turtle import *

radius = int(input("Enter the radius: "))
stepsLeft = int(input("Enter the max amount of steps: "))
trt = Turtle()
trt.speed(0)
trt.pendown()

# Drawing circle
itr = 150
angleStep = math.pi*2/itr
trt.penup()
trt.goto(radius,0)
trt.pendown()
offset = 0
for i in range(itr+1):
	trt.goto(math.cos(offset + i*angleStep)*radius, math.sin(offset + i*angleStep)*radius)
trt.penup()

# screenSize = (window_width(),window_height())
# Pirate routine
trt.goto(0,0)
trt.color('red')
trt.pendown()
trt.degrees()
while (trt.pos()[0]**2 + trt.pos()[1]**2 <= radius**2 and stepsLeft > 0):
    trt.setheading(random.uniform(-180, 180))
    trt.forward(20)
    stepsLeft -= 1

if(trt.pos()[0]**2 + trt.pos()[1]**2 > radius**2):
    print("Pirate has left the circle")
else:
    print("Pirate has reached the max amount of steps")
exitonclick()