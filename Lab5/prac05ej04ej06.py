import pygame
from pygame.locals import *
import sys

import math
import random

# Constants

CBOMB='B'
CFLAG='F'
CHIDDEN ='-'
SCREEN_W = 640
SCREEN_H = 480
WHITE = (255, 255, 255)

def CountBombs(tblHidden,x,y):
	amount = 0
	for i in range(-1,2):
		for j in range(-1,2):
			if(i != 0 or j != 0):#Center check
				cellCoor = (x+i, y+j)
				#Bounds check
				if(cellCoor[0] >= 0 and cellCoor[0] < len(tblHidden) and cellCoor[1] >= 0 and cellCoor[1] < len(tblHidden[0])):
					amount += 1 if tblHidden[cellCoor[0]][cellCoor[1]] == CBOMB else 0
	return amount
def ComputeBombs(tblHidden):#Mutator func
	for i in range(len(tblHidden)):
		for j in range(len(tblHidden[0])):
			if(tblHidden[i][j] != CBOMB):
				tblHidden[i][j] = CountBombs(tblHidden,i,j)

def PlaceBombs(tblHidden, bombAmt):#Mutator func
	width = len(tblHidden)
	height = len(tblHidden[0])
	while (bombAmt > 0):
		x = random.randint(0, width-1)
		y = random.randint(0, height-1)
		if(tblHidden[x][y] != CBOMB):
			tblHidden[x][y] = CBOMB
			bombAmt -= 1
def InitTable(rows, columns, bombAmt):
	tblHidden = []
	for i in range(columns):
		tblHidden.append([0]*rows)
	PlaceBombs(tblHidden,bombAmt)
	ComputeBombs(tblHidden)
	tblVisible = []
	for i in range(columns):
		tblVisible.append([CHIDDEN]*rows)
	return tblHidden, tblVisible
		
def ToggleFlag(tblVisible, x, y):
	if(tblVisible[x][y] == CHIDDEN):
		tblVisible[x][y] = CFLAG
	elif(tblVisible[x][y] == CFLAG):
		tblVisible[x][y] = CHIDDEN

def CloneMat(mat):
	newMat = []
	for i in range(len(mat)):
		row = []
		for j in range(len(mat[i])):
			row.append(mat[i][j])
		newMat.append(row)
	return newMat
hist = []
def RevealCellRecurs(tblVisible, tblHidden, x, y, origin): # returns the maximum distance reached from origin point
	tblVisible[x][y] = tblHidden[x][y]
	distSqr = (origin[0] - x)**2 + (origin[1] - y)**2
	if(tblHidden[x][y] != 0):
		return distSqr

	maxDist = distSqr
	for i in range(-1,2):
		for j in range(-1,2):
			if(i != 0 or j != 0):#Center check
				cellCoor = (x+i, y+j)
				#Bounds check
				if(cellCoor[0] >= 0 and cellCoor[0] < len(tblHidden) and cellCoor[1] >= 0 and cellCoor[1] < len(tblHidden[0])):
					if(tblVisible[cellCoor[0]][cellCoor[1]] == CHIDDEN): # hidden check
						maxDist = max(maxDist,RevealCellRecurs(tblVisible,tblHidden,cellCoor[0],cellCoor[1],origin))
	return maxDist
def RevealCell(tblVisible, tblHidden, x, y): # returns None on loss; otherwise return the max distance reached
	if(tblHidden[x][y] == CBOMB):
		return None
	return RevealCellRecurs(tblVisible, tblHidden, x, y, (x,y))
def isGameComplete(tblVisible, tblHidden):
	for i in range(len(tblVisible)):
		for j in range(len(tblVisible[i])):
			if(tblHidden[i][j] == CBOMB):
				if(tblVisible[i][j] != CFLAG):
					return False
			elif(tblVisible[i][j] == CHIDDEN):
				return False
	return True

def DrawTable(screen, tbl, tiles, spacing):
	for i in range(len(tbl)):
		for j in range(len(tbl[0])):
			screen.blit(tiles[str(tbl[i][j])], (i*spacing[0], j*spacing[1]))
def GetClickedCell(tableSpacing, offset, clickPoint):
	x = math.floor(clickPoint[0]/tableSpacing[0])
	y = math.floor(clickPoint[1]/tableSpacing[1])
	return (x,y)
def main():
	sys.setrecursionlimit(9999)
	tableWidth = 50
	tableHeight = 35
	bombAmount = 100
	h_tbl, v_tbl = InitTable(tableHeight,tableWidth,bombAmount)
	pygame.init()
	
	# Game speed init
	FPS = 60
	fpsClock = pygame.time.Clock()

	# tiles
	tiles = {
		"0": pygame.image.load('empty.png'),
		CHIDDEN: pygame.image.load('normal.png'),
		CBOMB: pygame.image.load('bomb.png'),
		CFLAG: pygame.image.load('flag.png')
	}
	for i in range(1,9):
		tiles[str(i)] = pygame.image.load(str(i) + '.png')
	tileSpacing = tiles['0'].get_size()

	# Screen init
	screen = pygame.display.set_mode((tableWidth*tileSpacing[0], tableHeight*tileSpacing[1]))
	pygame.display.set_caption('MineSweeper')


	revealDist = 0
	maxRevealDistSqr = 0
	curClick = None
	displayedTable = CloneMat(v_tbl)

	gameOver = False
	gameComplete = False
	gameRunning = True
	while gameRunning:
		#Screen clear
		screen.fill(WHITE) 

		# input
		for event in pygame.event.get():
			if event.type == QUIT:
				gameRunning = False
			if event.type == pygame.MOUSEBUTTONDOWN and not gameOver and not gameComplete and curClick == None:
				mousePos = pygame.mouse.get_pos()
				clickedCell = GetClickedCell(tileSpacing, (0,0), mousePos)
				
				if event.button == 1:
					curClick = clickedCell
					revealDist = 0
					distSqr = RevealCell(v_tbl,h_tbl,clickedCell[0],clickedCell[1])
					if(distSqr == None):
						distSqr = len(v_tbl)**2+ len(v_tbl[0])**2
						gameOver = True
						v_tbl = h_tbl
					maxRevealDistSqr = distSqr

				else:
					ToggleFlag(v_tbl, clickedCell[0], clickedCell[1])
					displayedTable = v_tbl
				if(not gameOver):
					gameComplete = isGameComplete(v_tbl, h_tbl)
		#Screen draw
		if(curClick != None):
			revealDist+=1
			for i in range(len(displayedTable)):
				for j in range(len(displayedTable[i])):## some optimizations could be made for this loop to oly iterate over cells in range
					vect = [i,j]
					vect[0] = curClick[0] - vect[0]
					vect[1] = curClick[1] - vect[1]
					if(vect[0]**2 + vect[1]**2 <= revealDist**2):
						displayedTable[i][j] = v_tbl[i][j]
			if(revealDist**2 > maxRevealDistSqr): # stops when maxDistance is reached
				displayedTable = CloneMat(v_tbl)
				curClick = None
				revealDist = 0
		DrawTable(screen, displayedTable, tiles, tileSpacing)

		
		# pygame display
		pygame.display.update()
		fpsClock.tick(FPS)


	pygame.quit()

if __name__ == "__main__":
	main()
