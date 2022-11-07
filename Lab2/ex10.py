from turtle import *
import math


itr = int(input("Enter the amount of sides: "))
side = float(input("Enter the side length: "))
# crcPerSide = int(input("Enter the amount of circles per side: "))
crcRadius = float(input("Enter the radius of a circle: "))

crcPerSide = int(side//(crcRadius*2))

trt = Turtle()

tracer(0, 0)
trt.radians()

crcItr = 20

polAngleStep = math.pi*2/itr
crcAngleStep = math.pi*2/crcItr


trt.pendown()
for i in range(itr):
	trtRot = i*polAngleStep
	trt.setheading(trtRot)
	
	# calculatring side outer normal vector
	normalVecX = math.sin(trtRot)*crcRadius
	normalVecY = -math.cos(trtRot)*crcRadius

	step = side/(crcPerSide)

	#circle centering
	trt.forward(step/2)

	for j in range(crcPerSide):
		
		
		trtPos = trt.pos()
		trt.penup()
		
		#calculating circle center
		crcCenterX = trtPos[0] + normalVecX
		crcCenterY = trtPos[1] + normalVecY

		#goto circle path start
		trt.goto(crcCenterX + crcRadius, crcCenterY)

		#drawing circle
		trt.pendown()
		for k in range(crcItr+1):
			trt.goto(crcCenterX + math.cos(k*crcAngleStep)*crcRadius, crcCenterY + math.sin(k*crcAngleStep)*crcRadius)
		trt.penup()

		#return to poly path
		trt.goto(trtPos[0], trtPos[1])
		trt.pendown()

		#move forward 1 step only if not last iter
		if(j < crcPerSide-1):
			trt.forward(step)
	
	#circle centering
	trt.forward(step/2)
		
trt.hideturtle()
update()

exitonclick()