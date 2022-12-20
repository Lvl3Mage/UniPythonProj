import pygame
from pygame.locals import *
import time
from random import randint

# Constantes para la inicialización de la superficie de dibujo
SCREEN_W = 640
SCREEN_H = 480
WHITE = (255, 255, 255)

def punto_dentro(posx,posy,dimx,dimy,x,y):
	dentro=True
	if x<posx:
		dentro=False
	if y<posy:
		dentro=False
	if x>(posx+dimx):
		dentro=False
	if y>(posy+dimy):
		dentro=False
	return dentro

def random_direction(direction):
	
	new=False
	while new==False:
		num = randint(1,4)
		new = True
		if num==1 :
			result="NE"
			if result==direction:
				new= False
		elif num==2 :
			result="SE"
			if result==direction:
				new= False
		elif num==3 :
			result="SO"
			if result==direction:
				new= False
		elif num==4 :
			result="NO"
			if result==direction:
				new= False
	return result
def main():
	# Inicialización de Pygame
	pygame.init()
	
	# Inicialización de la velocidad de refresco
	FPS = 60 
	fpsClock = pygame.time.Clock()
	
	# Inicialización de la superficie de dibujo (display surface)
	screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
	pygame.display.set_caption('Gato con animación y sonido')
	
	# Inicialización del sonido
	beep = pygame.mixer.Sound('beeps.wav')
	# Inicialización de la imagen del gato y del color del fondo
	cat = pygame.image.load('cat.png')
	cat_x = int(input("X inicial: "))
	cat_y = int(input("Y inicial: "))
	(cat_size_x, cat_size_y) = cat.get_size()
	
	# Bucle principal del juego
	finished = False
	direction = input("Dame direccion: ") 
	screen.fill(WHITE)
	while not finished: 
		previous_direction = direction
		if 'NE' in direction: 
			cat_x += 5
			cat_y += 5
			if cat_x+cat_size_x >= SCREEN_W or cat_y+cat_size_y >= SCREEN_H:
				previous_direction = direction
				direction = random_direction(previous_direction)
		if 'SE' in direction: 
			cat_y -= 5
			cat_x += 5
			if cat_y<=0 or cat_x+cat_size_x >= SCREEN_W:
				previous_direction = direction
				direction = random_direction(previous_direction)
		if 'SO' in direction: 
			cat_x -= 5
			cat_y -= 5
			if cat_x <= 0 or cat_y<=0:
				previous_direction = direction
				direction = random_direction(previous_direction)
		if 'NO' in direction: 
			cat_y += 5
			cat_x -= 5
			if cat_y+cat_size_y >= SCREEN_H or cat_x<=0:
				previous_direction = direction
				direction = random_direction(previous_direction)
		if previous_direction != direction:
			beep.play()
			time.sleep(1)
			beep.stop()
		# Copiar la imagen del gato a la superficie de dibujo
		screen.fill(WHITE)
		screen.blit(cat, (cat_x, cat_y))
		# Tratar los eventos (teclado, ratón, etc)
	
		
		for event in pygame.event.get():
			if event.type == QUIT:
				finished = True
			if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
				(click_pos_x,click_pos_y)=pygame.mouse.get_pos()
				dentro=punto_dentro(cat_x,cat_y,cat_size_x,cat_size_y,click_pos_x,click_pos_y)
				print(dentro)
				if dentro:
					direction = random_direction(previous_direction)
			
		# Visualizar en pantalla la superficie de dibujo
		pygame.display.update()
		fpsClock.tick(FPS)

main()