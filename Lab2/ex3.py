from turtle import *
import math


itr = int(input("Enter the amount of sides: "))
side = float(input("Enter the side length: "))

trt = Turtle()
trt.speed(0)

trt.degrees()
angleStep = 360/itr
trt.pendown()
offset = 0#angleStep/2
for i in range(itr):
    trt.setheading(offset + i*angleStep)
    trt.forward(side)
trt.hideturtle()


exitonclick()