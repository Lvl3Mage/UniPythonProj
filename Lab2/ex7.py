# import math
from turtle import *

dist = int(input("Enter the initial movement distance: "))
angleDif = float(input("Enter the angle increment: "))

acceleration = 2 
trt = Turtle()
trt.speed(0)
trt.penup()
screenSize = (window_width(),window_height())
trt.color('pink')
trt.shape('turtle')
# print(screenSize)
# trt.goto(screenSize[0],screenSize[1])
# trt.stamp()
while (abs(trt.pos()[0]) < screenSize[0]/2 and abs(trt.pos()[1]) < screenSize[1]/2):
    trt.stamp()
    trt.degrees()
    trt.setheading(trt.heading() + angleDif)
    trt.forward(dist)
    dist += acceleration
trt.hideturtle()
exitonclick()