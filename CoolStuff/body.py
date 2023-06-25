from turtle import *
import random
import math
import time
from Vector2 import Vector2
from Mathf import Mathf
class Body:
	G = 2000000
	attachedSim = None
	def __init__(self, ,radius, mass, velocity = Vector2.zero(), bounciness = 1):
		self.position = position
		self.radius = radius
		self.velocity = velocity
		self.mass = mass
		self.bounciness = bounciness
	def NewtoneanGrav(self):
		bodies = self.attachedSim._bodies
		for body in bodies:
			if(body != self):
				delta = body.position - self.position
				dist = delta.Length()
				# if(dist < 10):
				# 	continue
				accel = self.G*body.mass/(dist**2)
				self.velocity += delta.Normalized() * accel*self.attachedSim.deltaTime
	def EulerStep(self):
		# self.NewtoneanGrav()
		self.position += self.velocity*self.attachedSim.deltaTime
		
		# self.velocity += self.position*self.attachedSim.deltaTime*-1
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
	timeScale = 1
	stability = 1


	_bodies = []
	def __init__(self):
		self.deltaTime = self.fixedDeltaTime*self.timeScale/self.stability
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
	def ColVelElastic(self, velA, massA, velB, massB):
		totalMass = massA + massB
		v1 = ((massA - massB)/totalMass)*velA + (2*massB/totalMass)*velB
		return v1
	def ColVelNonElastic(self, velA, massA, velB, massB):
		return (velA * massA + velB * massB)/(massA+massB)
	def ResolveDynamic(self, bodyA, bodyB, normal):
		tangent = normal.PerpR()

		nVelA = Vector2.Dot(bodyA.velocity, normal)
		nVelB = Vector2.Dot(bodyB.velocity,normal)


		avBounciness = (bodyA.bounciness + bodyB.bounciness)/2
		_nVelNonElasticAB = self.ColVelNonElastic(nVelA, bodyA.mass, nVelB, bodyB.mass)

		_nVelElasticAB = self.ColVelElastic(nVelA, bodyA.mass, nVelB, bodyB.mass)
		_nVelElasticBA = self.ColVelElastic(nVelB, bodyB.mass, nVelA, bodyA.mass)

		_nVelA = Mathf.Lerp(_nVelNonElasticAB, _nVelElasticAB, avBounciness)
		_nVelB = Mathf.Lerp(_nVelNonElasticAB, _nVelElasticBA, avBounciness)

		tVelA = Vector2.Dot(bodyA.velocity, tangent)
		bodyA.velocity = tangent*tVelA + normal*_nVelA

		tVelB = Vector2.Dot(bodyB.velocity, tangent)
		bodyB.velocity = tangent*tVelB + normal*_nVelB
	def ResolveCollisions(self):
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
					self.ResolveDynamic(body,other,normal)

	def UpdateCycle(self):
		trt = Turtle()
		tracer(0, 0)
		trt.hideturtle()
		while trt:
			start = time.time()
			self.UpdateEuler()
			for i in range(10):
				self.ResolveCollisions()

			self.Draw(trt)
			end = time.time()
			executionTime = end - start
			self.deltaTime = max(executionTime,self.fixedDeltaTime*self.stability)*self.timeScale/self.stability
			print(1/max(self.fixedDeltaTime*self.stability, executionTime))

			time.sleep(max(self.fixedDeltaTime*self.stability - executionTime, 0))

def RandomVector():
	return Vector2(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0));
sim = Sim()

# sim.AddBody(Body(Vector2(0,0),15,5))
# sim.AddBody(Body(Vector2(-100,0), 5, 5, Vector2(0,100)))
# sim.AddBody(Body(Vector2(100,0), 5, 5, Vector2(0,-100)))
sim.AddBody(Body(Vector2(-100,0),15,15, Vector2.right()*600))
for i in range(50):
	vec = Vector2((i%10)*15*2,(i//10)*15*2 - 15*5)
	sim.AddBody(Body(vec, 10, 5))
	print(RandomVector())
sim.UpdateCycle()







# class Date:
# 	__init__(self,)