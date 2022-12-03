import pygame
from pygame.locals import *
import time

# Constantes para la inicialización de la superficie de dibujo
SCREEN_W = 640
SCREEN_H = 480
WHITE = (255, 255, 255)

def main():

	direction = input("Input a direction: ");
	posX = input("Input the initial x position:")
	posY = input("Input the initial y position:")
	pygame.init()
	
	# Game speed init
	FPS = 80
	fpsClock = pygame.time.Clock()
	
	# Screen init
	screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
	pygame.display.set_caption('Cat exercise')
	
	# Sound init
	beep = pygame.mixer.Sound('beeps.wav')

	# cat init
	cat = pygame.image.load('cat.png')
	cat_x = 10
	cat_y = 10
	(cat_size_x, cat_size_y) = cat.get_size()
	
	finished = False
	
	while not finished:
		#Screen clear
		screen.fill(WHITE) 

		# input
		for event in pygame.event.get():
			if event.type == QUIT:
				finished = True

		#Screen draw
		screen.blit(cat, (cat_x, cat_y))
		

		
		# pygame display
		pygame.display.update()
		fpsClock.tick(FPS)


	pygame.quit()

if __name__ == '__main__':
	main()
