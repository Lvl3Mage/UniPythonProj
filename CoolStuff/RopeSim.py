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
			trt.color((200,122,122))
		else:
			trt.color((122,122,122))
		trt.dot(6)
	def Highlight(self, trt):
		trt.color((0,0,0))
		trt.penup()
		trt.goto(self.position.x, self.position.y - 10)
		trt.pendown()
		trt.circle(10)
class Constraint:
	def __init__(self,pointA, pointB, length = None, strength = 0.9):

		self.pointA = pointA
		self.pointB = pointB
		self.strength = strength
		if(length == None):
			self.length = (pointA.position - pointB.position).Length()
		else:
			self.length = length
	def __str__(self):
		return "Constraint between {0} - {1}".format(pointA,pointB)
	def Update(self):
		curLengthSqr = (self.pointB.position - self.pointA.position).LengthSqr()
		if(curLengthSqr > (self.length*(1/(1-self.strength)))**2 or curLengthSqr < (self.length*(1-self.strength))**2):
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

points = []
constraints = []
draggedPointPrevState = False
draggedPoint = None
SimRunning = False
screenSize = None

selectedPoint = None

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
	global draggedPointPrevState
	if(draggedPoint == None):
		clickPoint = Vector2(x,y)
		closestId = closestPointID(clickPoint)
		if(closestId >= 0):
			distSqr = (points[closestId].position - clickPoint).LengthSqr()
			if(distSqr < 45**2):
				
				draggedPoint = points[closestId]
				draggedPointPrevState = draggedPoint.locked
				draggedPoint.locked = True
	else:
		draggedPoint.locked = draggedPointPrevState
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
	global selectedPoint
	trt.clear()
	if(selectedPoint != None):
		selectedPoint.Highlight(trt)
	for constraint in constraints:
		constraint.Draw(trt)
	for point in points:
		point.Draw(trt)
	print(selectedPoint)
	

def AddPointAt(x,y):
	global selectedPoint
	clickPoint = Vector2(x,y)
	closestId = closestPointID(clickPoint)
	if(closestId >= 0):
		distSqr = (points[closestId].position - clickPoint).LengthSqr()
		if(distSqr < 15**2):
			if(selectedPoint != None):
				if(selectedPoint != points[closestId]):
					PointToPointConstraint(selectedPoint, points[closestId])
					selectedPoint = points[closestId]
				else:
					selectedPoint = None	
			else:
				selectedPoint = points[closestId]
			RedrawScene()
			return

	newPoint = Point(clickPoint)
	if(selectedPoint != None):
		PointToPointConstraint(selectedPoint, newPoint)
		selectedPoint = newPoint
	points.append(newPoint)
	RedrawScene()

def PointToPointConstraint(pointA, pointB):
	if(pointA == pointB):
		return
	constraintExists = False
	for constraint in constraints:
		if(constraint.pointA == pointA and constraint.pointB == pointB or constraint.pointA == pointB and constraint.pointB == pointA):
			constraintExists = True
			break
	if(not constraintExists):
		constraints.append(Constraint(pointA, pointB))
	else:
		print("Constraint exists")
def CreateConstraintTo(x, y):
	global selectedPoint
	clickPoint = Vector2(x,y)
	closestId = closestPointID(clickPoint)
	if(closestId >= 0):
		distSqr = (points[closestId].position - clickPoint).LengthSqr()
		if(distSqr < 15**2):
			points[closestId].locked = not points[closestId].locked
			RedrawScene()
		else:
			selectedPoint = None
			RedrawScene()

def RemovePointAt(x, y):
	global selectedPoint
	clickPoint = Vector2(x,y)

	closestId = closestPointID(clickPoint)
	if(closestId >= 0):
		distSqr = (points[closestId].position - clickPoint).LengthSqr()
		if(distSqr < 15**2):
			closestPoint = points[closestId]
			for i in range(len(constraints)-1, -1, -1):
				if(constraints[i].pointA == closestPoint or constraints[i].pointB == closestPoint):
					constraints.pop(i)
			if(selectedPoint == closestPoint):
				selectedPoint = None
			points.pop(closestId)
			RedrawScene()
			return

def ToggleSim():
	global SimRunning

	if(SimRunning):
		SimRunning = False
		EnableEditor()
	else:
		SimRunning = True
		DisableEditor()
		UpdateCycle(points, constraints, trt)

def AddMatrix(rows, columns, spacing):
	global points, constraints
	matPoints = []
	for i in range(rows):
		for j in range(columns):
			lock = False
			if(i == 0):
				lock = j % 5 == 0 or j == columns-1
			matPoints.append(Point(Vector2((j-(columns/2))*spacing,(-i+(rows/2))*spacing), lock))
	points += matPoints
	matConstraints = []
	for i in range(rows):
		for j in range(columns):
			if(j < columns-1):
				matConstraints.append(Constraint(matPoints[columns*i+ j],matPoints[columns*i+j+1]))
			if(i < (rows - 1)):
				matConstraints.append(Constraint(matPoints[columns*i + j],matPoints[columns*i+j+columns]))
	constraints += matConstraints
AddMatrix(15,5,15)


def EnableEditor():
	global draggedPoint, draggedPointPrevState
	if(draggedPoint != None):
		draggedPoint.locked = draggedPointPrevState
		draggedPoint = None
	global selectedPoint
	selectedPoint = None
	screen.onclick(AddPointAt,  btn=1)
	screen.onclick(RemovePointAt, btn=2)
	screen.onclick(CreateConstraintTo, btn=3)
	RedrawScene()

def DisableEditor():
	screen.onclick(ToggleDrag, btn=1)
	screen.onclick(None, btn=2)
	screen.onclick(None, btn=3)


EnableEditor()
screen.onkey(ToggleSim, 'space')


screen.listen()
mainloop()