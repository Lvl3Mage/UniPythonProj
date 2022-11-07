from turtle import *
import math



side = int(input("Enter step size: "))
count = int(input("Enter step amount: "))

trt = Turtle()
trt.speed(0)
trt.goto(0,0)
trt.pendown()
for i in range(0,count):
    trt.goto(-side*i, side*(i+1))
    trt.goto(-side*(i+1), side*(i+1))

trt.goto(-side*count, 0)
trt.goto(0, 0)
trt.hideturtle()


exitonclick()




