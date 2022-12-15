from turtle import *
import random
import math
import time
from Vector2 import Vector2
class Body:
	G = 2000000
	attachedSim = None
	def __init__(self,position,radius, mass, velocity = Vector2.zero()):
		self.position = position
		self.radius = radius
		self.velocity = velocity
		self.mass = mass
	def NewtoneanGrav(self):
		global Energy
		bodies = self.attachedSim._bodies
		for body in bodies:
			if(body != self):
				delta = body.position - self.position
				dist = delta.Length()
				# if(dist < 10):
				# 	continue
				accel = self.G*body.mass/(dist**2)
				# Energy -= (self.G*self.mass*body.mass)/dist
				self.velocity += delta.Normalized() * accel*self.attachedSim.deltaTime
	def EulerStep(self):
		global Energy
		self.NewtoneanGrav()
		self.position += self.velocity*self.attachedSim.deltaTime
		Energy += self.mass*(self.velocity.Length()**2)*0.5
		
		# self.velocity += self.position*self.attachedSim.deltaTime*-1
	def Draw(self, trt):
		trt.penup()
		trt.goto(self.position.x, self.position.y)
		trt.pendown()
		trt.circle(self.radius)
		trt.penup()
	def AttachToSim(self, sim):
		self.attachedSim = sim

Energy = 0
class Sim:
	fixedDeltaTime = 0.02
	precision = 1


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

		_nVelA = self.ColVelNonElastic(nVelA, bodyA.mass, nVelB, bodyB.mass)
		_nVelB = self.ColVelNonElastic(nVelB, bodyB.mass, nVelA, bodyA.mass)

		tVelA = Vector2.Dot(bodyA.velocity, tangent)
		bodyA.velocity = tangent*tVelA + normal*_nVelA

		tVelB = Vector2.Dot(bodyB.velocity, tangent)
		bodyB.velocity = tangent*tVelB + normal*_nVelB
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
					self.ResolveDynamic(body,other,normal)

	def UpdateCycle(self):
		global Energy
		trt = Turtle()
		tracer(0, 0)
		trt.hideturtle()
		while trt:
			start = time.time()
			Energy = 0
			self.UpdateEuler()
			self.ResolveStatic()

			self.Draw(trt)
			print(Energy)
			end = time.time()
			executionTime = end - start
			self.deltaTime = max(executionTime,self.fixedDeltaTime*self.precision)/5
			# print(max(self.fixedDeltaTime*self.precision - executionTime, 0))

			time.sleep(max(self.fixedDeltaTime*self.precision - executionTime, 0))

def RandomVector():
	return Vector2(random.uniform(-1.0,1.0),random.uniform(-1.0,1.0));
sim = Sim()

# sim.AddBody(Body(Vector2(0,0),15,5))
sim.AddBody(Body(Vector2(-100,0), 5, 5, Vector2(0,100)))
sim.AddBody(Body(Vector2(100,0), 5, 5, Vector2(0,-100)))
# sim.AddBody(Body(Vector2(-100,0),15,15, Vector2.right()*600))
# for i in range(2):
# 	vec = Vector2((i%10)*15*2,(i//10)*15*2 - 15*5)
# 	sim.AddBody(Body(vec, 5, 5))
	# print(RandomVector())
sim.UpdateCycle()







# class Date:
# 	__init__(self,)