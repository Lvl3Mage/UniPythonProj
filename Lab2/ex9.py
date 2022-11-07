import random
from turtle import *

n = int(input("Enter the amount of iterations: "))
trt = Turtle()
trt.speed(0)
trt.pendown()
screenSize = (window_width(),window_height())
cont = True # Could have use break for this lol
while (cont):
    for i in range(n):
        trt.width(random.uniform(1,20))
        trt.pencolor(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
        
        x = random.uniform(-screenSize[0]/2, screenSize[0]/2)
        y = random.uniform(-screenSize[1]/2, screenSize[1]/2)
        trt.goto(x,y)
    cont = input("Would you like to continue? (Y/N) >> ").lower() == 'y'
trt.hideturtle()
exitonclick()