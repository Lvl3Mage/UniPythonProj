from turtle import *
import time
import random
from Vector2 import Vector2
class Point:
	collisionPadding = 10
	gravity = Vector2.down()*9.81*100
	def __init__(self,position, locked = False):
		self.position = position
		self.prevPosition = position
		self.locked = locked
	def __str__(self):
		return str(self.position)
	def EulerStep(self, deltaTime):
		if(not self.locked):
			newPrevPosition = self.position
			self.position += self.position - self.prevPosition
			self.position += Point.gravity * deltaTime * deltaTime

			#wall collisions
			self.position.y = min(max(self.position.y, -screenSize.y/2 +  Point.collisionPadding),screenSize.y/2- Point.collisionPadding)
			newPrevPosition.y = min(max(newPrevPosition.y, -screenSize.y/2 +  Point.collisionPadding),screenSize.y/2 -  Point.collisionPadding)
			self.position.x = min(max(self.position.x, -screenSize.x/2 +  Point.collisionPadding),screenSize.x/2- Point.collisionPadding)
			newPrevPosition.x = min(max(newPrevPosition.x, -screenSize.x/2 +  Point.collisionPadding),screenSize.x/2 -  Point.collisionPadding)

			self.prevPosition = newPrevPosition
		elif(draggedPoint == self):
			self.prevPosition = self.position
	def Draw(self,trt):
		trt.penup()
		trt.goto(self.position.x, self.position.y)
		trt.pendown()
		if(self.locked):
			trt.dot(6, (200,122,122))
		else:
			trt.dot(6, (122,122,122))
class Constraint:
	def __init__(self,pointA, pointB, length = None):

		self.pointA = pointA
		self.pointB = pointB
		if(length == None):
			self.length = (pointA.position - pointB.position).Length()
		else:
			self.length = length
	def __str__(self):
		return "Constraint between {0} - {1}".format(pointA,pointB)
	def Update(self):
		if((self.pointB.position - self.pointA.position).Length() > self.length*2):
			for i in range(len(constraints)):
				if(constraints[i] == self):
					constraints.pop(i)
					break
		if(self.pointA.locked and self.pointB.locked):
			pass
		elif(self.pointA.locked):
			self.pointB.position = self.pointA.position + (self.pointB.position - self.pointA.position).Normalized()*self.length
		elif(self.pointB.locked):
			self.pointA.position = self.pointB.position + (self.pointA.position - self.pointB.position).Normalized()*self.length
		else:
			delta = self.pointB.position - self.pointA.position
			if(delta.LengthSqr() < 0.001):
				return
			newCentralVector = delta.Normalized()*(self.length/2)
			center = (self.pointA.position + self.pointB.position)*0.5
			self.pointA.position = center - newCentralVector
			self.pointB.position = center + newCentralVector
	def Draw(self, trt):
		trt.penup()
		trt.goto(self.pointA.position.x, self.pointA.position.y)
		trt.color(200,200,200)
		trt.pendown()
		trt.goto(self.pointB.position.x, self.pointB.position.y)



trt = Turtle()
tracer(0, 0)
trt.hideturtle()
screen = Screen()
screen.colormode(255)
canvas = getcanvas()
connectionPoint = None
points = []
constraints = []
draggedPointWasLocked = False
draggedPoint = None
SimRunning = False
screenSize = None
connectedMode = False
prevPlacedPoint = None

def UpdateCycle(points, constraints, trt):
	global screenSize
	fixedDeltaTime = 0.01
	constraintIterCount = 10

	avFps = 1/fixedDeltaTime
	deltaTime = fixedDeltaTime
	while SimRunning:
		screenSize = Vector2(window_width(),window_height())
		start = time.time()
		trt.clear()
		for point in points:
			point.EulerStep(deltaTime)
		if(draggedPoint != None):
			target = Vector2(canvas.winfo_pointerx() - canvas.winfo_rootx(), -(canvas.winfo_pointery() - canvas.winfo_rooty()))
			
			target.y += screenSize.y*0.5
			target.x -= screenSize.x*0.5
			draggedPoint.position = target
		
		for i in range(constraintIterCount):
			for constraint in constraints:
				constraint.Update()

		for point in points:
			point.Draw(trt)

		for constraint in constraints:
			constraint.Draw(trt)
		update()
		end = time.time()
		executionTime = end - start
		deltaTime = max(executionTime,fixedDeltaTime)
		avFps = (avFps + 1/deltaTime)/2
		print(avFps)
		time.sleep(max(fixedDeltaTime - executionTime, 0))









def closestPointID(pos):
	closestId = -1
	closestDistSqr = float('inf')
	for i in range(len(points)):
		distSqr = (points[i].position - pos).LengthSqr()

		if(distSqr < closestDistSqr):
			closestDistSqr = distSqr
			closestId = i
	return closestId

def ToggleDrag(x,y):
	global draggedPoint
	global draggedPointWasLocked
	if(draggedPoint == None):
		clickPoint = Vector2(x,y)
		closestId = closestPointID(clickPoint)
		if(closestId >= 0):
			distSqr = (points[closestId].position - clickPoint).LengthSqr()
			if(distSqr < 45**2):
				
				draggedPoint = points[closestId]
				draggedPointWasLocked = draggedPoint.locked
				draggedPoint.locked = True
	else:
		draggedPoint.locked = draggedPointWasLocked
		draggedPoint = None
# Interseciton code
	# def intersection(p1,dir1,p2,dir2):
	# 	m1 = dir1.y/dir1.x
	# 	m2 = dir2.y/dir2.x

	# 	n1 = p1.x/dir1.x
	# 	n2 = p2.x/dir2.x

	# 	x = (n2-n1)/(m1-m2)
	# 	y = (dir1.y * x + p1.x)/dir1.x
	# 	return Vector2(x,y)

# EDITOR
def RedrawScene():
	trt.clear()
	for constraint in constraints:
		constraint.Draw(trt)
	for point in points:
		point.Draw(trt)


def clickLeft(x, y):
	global connectedMode
	global prevPlacedPoint
	clickPoint = Vector2(x,y)
	closestId = closestPointID(clickPoint)
	if(closestId >= 0):
		distSqr = (points[closestId].position - clickPoint).LengthSqr()
		if(distSqr < 15**2):
			points[closestId].locked = not points[closestId].locked
			RedrawScene()
			return

	newPoint = Point(clickPoint)
	# check if clicking on point -- toggle point lock
	if(connectedMode):
		if(prevPlacedPoint != None):
			constraints.append(Constraint(prevPlacedPoint, newPoint))
		prevPlacedPoint = newPoint
	points.append(newPoint)
	RedrawScene()

def clickRight(x, y):
	global connectionPoint
	clickPoint = Vector2(x,y)
	closestId = closestPointID(clickPoint)
	if(closestId >= 0):
		distSqr = (points[closestId].position - clickPoint).LengthSqr()
		if(distSqr < 15**2):
			print(connectionPoint)
			if(connectionPoint == None):
				connectionPoint = points[closestId]
			else:
				if(connectionPoint != points[closestId]):

					constraints.append(Constraint(connectionPoint, points[closestId]))
					connectionPoint = None
					RedrawScene()

def clickMiddle(x, y):
	global connectionPoint
	global prevPlacedPoint
	clickPoint = Vector2(x,y)

	closestId = closestPointID(clickPoint)
	if(closestId >= 0):
		distSqr = (points[closestId].position - clickPoint).LengthSqr()
		if(distSqr < 15**2):
			closestPoint = points[closestId]
			for i in range(len(constraints)-1, -1, -1):
				if(constraints[i].pointA == closestPoint or constraints[i].pointB == closestPoint):
					constraints.pop(i)
			if(connectionPoint == closestPoint):
				connectionPoint = None
			if(prevPlacedPoint == closestPoint):
				prevPlacedPoint = None
			points.pop(closestId)
			RedrawScene()
			return
	# minConDistSqr = float('inf')
	# minConID = -1
	# for i in range(len(constraints)):
	# 	conDir = constraints[i].pointB.position - constraints[i].pointA.position
	# 	interectPoint = intersection(constraints[i].pointA.position, conDir, clickPoint, conDir.PerpL())
	# 	print(interectPoint)
	# 	distSqr = (clickPoint - interectPoint).LengthSqr()
	# 	if(distSqr < minConDistSqr):
	# 		minConID = i
	# 		minConDistSqr = distSqr
	# print(minConDistSqr)
	# if(minConID >= 0):
	# 	if(minConDistSqr < 15**2):
	# 		constraints.pop(minConID)
	# 		RedrawScene()

def ToggleSim():
	global SimRunning

	if(SimRunning):
		SimRunning = False
		EnableEditor()
	else:
		SimRunning = True
		DisableEditor()
		UpdateCycle(points, constraints, trt)


def ToggleConnectedMode():
	global connectedMode
	global prevPlacedPoint
	connectedMode = not connectedMode
	prevPlacedPoint = None
def EnableEditor():
	global connectionPoint
	connectionPoint = None
	prevPlacedPoint = None
	screen.onclick(clickLeft,  btn=1)
	screen.onclick(clickMiddle, btn=2)
	screen.onclick(clickRight, btn=3)
	screen.onkey(ToggleConnectedMode, 'c')

def DisableEditor():
	screen.onclick(ToggleDrag, btn=1)
	screen.onclick(None, btn=2)
	screen.onclick(None, btn=3)
	screen.onkey(None, 'c')


EnableEditor()
screen.onkey(ToggleSim, 'space')


screen.listen()
mainloop()