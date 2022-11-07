from turtle import *
import random
import math
import time
from Vector2 import Vector2
class Body:
	attachedSim = None
	def __init__(self,position,radius, mass, velocity = Vector2.zero()):
		self.position = position
		self.radius = radius
		self.velocity = velocity
		self.mass = mass

	def EulerStep(self):
		self.position += self.velocity*self.attachedSim.deltaTime
		self.velocity += self.position*self.attachedSim.deltaTime*-1
	def Draw(self, trt):
		trt.penup()
		trt.goto(self.position.x, self.position.y)
		trt.pendown()
		trt.circle(self.radius)
		trt.penup()
	def AttachToSim(self, sim):
		self.attachedSim = sim

class Sim:
	fixedDeltaTime = 0.02


	_bodies = []
	def __init__(self):
		self.deltaTime = self.fixedDeltaTime
		pass
	def AddBody(self, body):
		self._bodies.append(body)
		body.AttachToSim(self)
	def UpdateEuler(self):
		for body in self._bodies:
			body.EulerStep()
	def Draw(self, trt):
		trt.clear()
		for body in self._bodies:
			body.Draw(trt)
		update()
	def ResolveStatic(self):
		for body in self._bodies:
			for other in self._bodies:
				if(other == body):
					continue
				delta = other.position - body.position
				distanceSqr = delta.LengthSqr()
				minDistance = body.radius + other.radius
				if(distanceSqr < minDistance**2):
					distance = math.sqrt(distanceSqr)
					normal = delta.Normalized()
					totalMass = body.mass + other.mass
					intersection = minDistance - distance
					body.position -= normal*intersection*(body.mass/totalMass)
					other.position += normal*intersection*(other.mass/totalMass)

	def UpdateCycle(self):
		trt = Turtle()
		tracer(0, 0)
		trt.hideturtle()
		while trt:
			start = time.time()

			self.UpdateEuler()
			self.ResolveStatic()

			self.Draw(trt)

			end = time.time()
			executionTime = end - start
			self.deltaTime = max(executionTime,self.fixedDeltaTime)
			print(max(self.fixedDeltaTime - executionTime, 0))

			time.sleep(max(self.fixedDeltaTime - executionTime, 0))


sim = Sim()

for i in range(50):
	vec = Vector2(random.uniform(-40, 40),random.uniform(-40, 40))
	sim.AddBody(Body(vec, 15, 5, Vector2(random.uniform(-1, 1),random.uniform(-1, 1))*100))
sim.UpdateCycle()