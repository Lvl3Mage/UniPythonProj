from turtle import *
import time
from Vector2 import Vector2

def DrawChain(chain, trt):
	trt.penup()
	trt.goto(chain[0].x,chain[0].y)
	trt.pendown()
	for i in range(1, len(chain)):
		# print(chain[i])
		
		trt.goto(chain[i].x,chain[i].y)
def RunConstraint(points,lengths):
	#backward loop from penultimate index to index 1
	for i in range(len(points)-2, 0, -1):
		delta = points[i] - points[i+1] #delta between current and next
		points[i] = points[i+1] + delta.Normalized()*lengths[i-1]

	#forward loop starting with index 1 and ending in last index
	for i in range(1, len(points)):
		delta = points[i] - points[i-1]  #delta between current and previous
		points[i] = points[i-1] + delta.Normalized()*lengths[i-1]
def RunFabrik(points, lengths, target):
	points[len(points)-1] = target # set last point in sequence to target
	RunConstraint(points,lengths)

def Gravity(points):
	for i in range(1,len(points)):
		points[i] += Vector2.down()*0.02*500



deltaTime = 0.02
ropeLength = 500
ropeJoints = 100

lengths = []
ropeDelta = ropeLength/ropeJoints
for i in range(ropeJoints):
	lengths.append(ropeDelta)

points = [Vector2.zero()]
for i in range(len(lengths)):
	points.append(points[i] + Vector2.right()*lengths[i])

trt = Turtle()
tracer(0, 0)
trt.hideturtle()
canvas = getcanvas()
while trt:
	trt.clear()
	start = time.time()
	target = Vector2(canvas.winfo_pointerx() - canvas.winfo_rootx(), -(canvas.winfo_pointery() - canvas.winfo_rooty()))
	screenSize = Vector2(window_width(),window_height())
	target.y += screenSize.y*0.5
	target.x -= screenSize.x*0.5
	# print(target)
	# target += screenSize*0.5
	# trt.goto(target.x, target.y)
	# 
	Gravity(points)
	RunFabrik(points, lengths, target)
	DrawChain(points,trt)
	end = time.time()
	executionTime = end - start
	update()
	time.sleep(max(deltaTime - executionTime, 0))
