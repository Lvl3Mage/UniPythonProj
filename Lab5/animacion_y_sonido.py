import pygame
from pygame.locals import *
import time
import random
from Vector2 import Vector2
from Mathf import Mathf
#Constants
SCREEN_W = 640
SCREEN_H = 480
WHITE = (255, 255, 255)

def CatBounce(initialPosition, initialAngle, catVelocityScalar):
	pygame.init()
	
	# Game speed init
	FPS = 60
	fpsClock = pygame.time.Clock()



	# Asset setup
	beep = pygame.mixer.Sound('beeps.wav')
	catSprite = pygame.image.load('cat.png')


	catSize = catSprite.get_size()
	catSize = Vector2(catSize[0], catSize[1])

	# Screen init
	screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
	pygame.display.set_caption('Cat Bounce')


	#### Runtime Data ####
	gameRunning = True
	catPosition = Vector2(initialPosition.x, initialPosition.y)
	catVelocity = Vector2.down().RotateByAngle(initialAngle)*catVelocityScalar

	soundTimer = 0

	while gameRunning:
		### Screen clear ###
		screen.fill(WHITE) 

		### Input handling ###
		for event in pygame.event.get():
			#Game exit
			if event.type == QUIT:
				gameRunning = False

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 

				#Mouse position
				mousePos = pygame.mouse.get_pos()
				mousePos = Vector2(mousePos[0], mousePos[1])

				mousePosClampled = Vector2(Mathf.Clamp(mousePos.x, catPosition.x, catPosition.x + catSize.x),Mathf.Clamp(mousePos.y, catPosition.y, catPosition.y + catSize.y))
				if(mousePos.isEqual(mousePosClampled)):
					catVelocity = catVelocity.RotateByAngle(random.randint(1,2)*90)

					#initiating sound
					beep.play()
					soundTimer = 4
		## Update ##

		if(soundTimer > 0):
			soundTimer -= 1/FPS
		else:
			soundTimer = 0
			beep.stop()



		catPosition += catVelocity

		clampedPosition = Vector2(Mathf.Clamp(catPosition.x, 0, SCREEN_W - catSize.x),Mathf.Clamp(catPosition.y, 0, SCREEN_H - catSize.y))

		delta = clampedPosition - catPosition
		
		if(delta.LengthSqr() > 0):# collision with wall

			# snapping delta to 45 degree directions
			if(delta.x != 0):
				delta.x = delta.x/abs(delta.x)
			if(delta.y != 0):
				delta.y = delta.y/abs(delta.y)

			#normal and tangent calculation
			normal = delta.Normalized()
			tangent = normal.PerpR()

			# projectiong global cat velocity to local normal and tangent scalars 
			normalVel = -Vector2.Dot(catVelocity, normal)
			tangentVel = Vector2.Dot(catVelocity, tangent)

			#local bounce velocity along normal and tangent vectors
			localBounceVel = Vector2(tangentVel, normalVel)

			# computing global up and right axis to local normal and tangent space
			localYAxis = Vector2(Vector2.Dot(Vector2.up(), tangent), Vector2.Dot(Vector2.up(), normal))
			localXAxis = localYAxis.PerpR()

			

			
			#computing the final cat velocity along the global axis
			catVelocity = Vector2(Vector2.Dot(localBounceVel, localXAxis), Vector2.Dot(localBounceVel, localYAxis))
			
			#clamping the cat position (yes this is a little incorrect and the cat will drift when the delta is high enough)
			catPosition = clampedPosition

			#initiating sound
			beep.play()
			soundTimer = 4



		## Screen draw ##
		screen.blit(catSprite, (catPosition.x, catPosition.y))

		
		# pygame display
		pygame.display.update()
		fpsClock.tick(FPS)


	pygame.quit()

if __name__ == '__main__':
	initialPositionX = float(input("Enter the X coordinate of the cat: "))
	initialPositionY = float(input("Enter the Y coordinate of the cat: "))

	angle = 0
	direction = input("Enter the direction of the cat (NE, SE, SW, NW or the angle in degrees): ").upper()
	# would be much easier to use a dict here
	if(direction == "NE"):
		angle = 45
	elif(direction == "SE"):
		angle = 135
	elif(direction == "SW"):
		angle = 225
	elif(direction == "NW"):
		angle = 315
	else:
		angle = float(direction)

	speed = float(input("Enter the speed of the cat:"))
	CatBounce(Vector2(initialPositionX,initialPositionY), angle, speed)
