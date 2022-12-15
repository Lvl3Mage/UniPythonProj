import pygame
from pygame.locals import *
import sys

import math
import random

import tkinter.simpledialog

### Constants ###

CBOMB='B'
CFLAG='F'
CHIDDEN ='-'
WHITE = (255, 255, 255)


### Table Init Funcs ###
def CountBombs(tblHidden,x,y): # counts the amount bombs cells adjacent to the specified cell
	amount = 0
	for i in range(-1,2):
		for j in range(-1,2):
			if(i != 0 or j != 0):#Center check
				cellCoor = (x+i, y+j)
				#Bounds check
				if(cellCoor[0] >= 0 and cellCoor[0] < len(tblHidden) and cellCoor[1] >= 0 and cellCoor[1] < len(tblHidden[0])):
					amount += 1 if tblHidden[cellCoor[0]][cellCoor[1]] == CBOMB else 0
	return amount

def ComputeBombCounts(tblHidden):#Mutator func, computes the bomb counts for each cell in a given table
	for i in range(len(tblHidden)):
		for j in range(len(tblHidden[0])):
			if(tblHidden[i][j] != CBOMB):
				tblHidden[i][j] = CountBombs(tblHidden,i,j)

def PlaceBombs(tblHidden, bombAmt):#Mutator func, places a cetrain amount of bombs on the given table
	width = len(tblHidden)
	height = len(tblHidden[0])
	while (bombAmt > 0):
		x = random.randint(0, width-1)
		y = random.randint(0, height-1)
		if(tblHidden[x][y] != CBOMB):
			tblHidden[x][y] = CBOMB
			bombAmt -= 1

def InitMineSweeperTable(rows, columns, bombAmt): #Initiates a minesweeper table with specified rows, columns and bomb amount, returns a tuple of the hidden table and a visible table
	tblHidden = []
	for i in range(columns):
		tblHidden.append([0]*rows)
	PlaceBombs(tblHidden,bombAmt)
	ComputeBombCounts(tblHidden)
	tblVisible = []
	for i in range(columns):
		tblVisible.append([CHIDDEN]*rows)
	return tblHidden, tblVisible


### Action Funcs ###
def ToggleFlag(tblVisible, x, y, curFlagsAmt, totalBombs):#Mutator func, toggles the flag on the specified cell, returns the new amount of flags
	if(tblVisible[x][y] == CHIDDEN and totalBombs > curFlagsAmt):
		tblVisible[x][y] = CFLAG
		curFlagsAmt+=1
	elif(tblVisible[x][y] == CFLAG):
		tblVisible[x][y] = CHIDDEN
		curFlagsAmt-=1
	return curFlagsAmt

def GetClickedCellCoords(tableSpacing, clickPoint): # Returns the x and y indecies of the clicked cell
	x = math.floor(clickPoint[0]/tableSpacing[0])
	y = math.floor(clickPoint[1]/tableSpacing[1])
	return (x,y)

def RevealCellRecurs(tblVisible, tblHidden, x, y, origin):#Mutator func, recursively reveals cells of a table, returns the maximum distance reached from origin point
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
					cellValue = tblVisible[cellCoor[0]][cellCoor[1]]

					##TODO this will ignore flags so some areas could get blocked of
					##Implementing flag clearing requires the modification of the flag count var in the Minesweeper func
					##A solution could be implementing Minesweeper as a class and changing the flag count variable to classwide variable 
					if(cellValue == CHIDDEN): # hidden check 
						maxDist = max(maxDist,RevealCellRecurs(tblVisible,tblHidden,cellCoor[0],cellCoor[1],origin))
	return maxDist

def RevealCell(tblVisible, tblHidden, x, y):#Mutator func, starter action for a reveal sequence. Returns None on loss; otherwise return the max distance reached
	if(tblVisible[x][y] == CFLAG):
		return 0
	if(tblHidden[x][y] == CBOMB):
		return None
	return RevealCellRecurs(tblVisible, tblHidden, x, y, (x,y))


### Misc Funcs ###
def CloneMat(mat):
	newMat = []
	for i in range(len(mat)):
		row = []
		for j in range(len(mat[i])):
			row.append(mat[i][j])
		newMat.append(row)
	return newMat

def isGameComplete(tblVisible, tblHidden): #Checks whether a visible table is a solution for a hidden table
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

### Main Gameloop ###
def MineSweeper(tableWidth, tableHeight, bombAmount):

	sys.setrecursionlimit(9999)

	#Table init
	h_tbl, v_tbl = InitMineSweeperTable(tableHeight,tableWidth,bombAmount)

	pygame.init()
	
	# Game speed init
	FPS = 60
	fpsClock = pygame.time.Clock()

	# Tile setup
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


	#### Runtime Data ####

	flagAmount = 0

	#Reveal effect data
	curRevealOrigin = None
	lastClickedCell = None
	curRevealDist = 0
	maxRevealDistSqr = 0
	
	gameCompleteCounter = 0
	displayedTable = CloneMat(v_tbl)

	#Game flags
	gameOver = False
	gameComplete = False
	gameRunning = True

	while gameRunning:
		### Screen clear ###
		screen.fill(WHITE) 

		### Input handling ###
		for event in pygame.event.get():
			#Game exit
			if event.type == QUIT:
				gameRunning = False

			# No mouse events will be processed if game is over/complete or if the reveal effect is still ongoing
			if event.type == pygame.MOUSEBUTTONDOWN and not gameOver and not gameComplete and curRevealOrigin == None: 

				#Mouse position
				mousePosUnclamped = pygame.mouse.get_pos()
				#Clamping to screen size
				mousePos = [mousePosUnclamped[0], mousePosUnclamped[1]]
				mousePos[0] = max(min(mousePos[0], (len(v_tbl)-1) * tileSpacing[0]), 0)
				mousePos[1] = max(min(mousePos[1], (len(v_tbl[0])-1) * tileSpacing[1]), 0)
				#Clicked cell indecies
				clickedCell = GetClickedCellCoords(tileSpacing, mousePos)
				
				if event.button == 1:
					#Reveal Setup
					curRevealOrigin = clickedCell
					curRevealDist = 0
					distSqr = RevealCell(v_tbl,h_tbl,clickedCell[0],clickedCell[1])#sets max distance reveal dist

					if(distSqr == None):#Bomb clicked
						distSqr = len(v_tbl)**2+ len(v_tbl[0])**2
						gameOver = True
						v_tbl = h_tbl
					maxRevealDistSqr = distSqr

				else:
					#Flag toggle
					flagAmount = ToggleFlag(v_tbl, clickedCell[0], clickedCell[1], flagAmount, bombAmount)
					displayedTable = CloneMat(v_tbl)

				if(not gameOver):
					gameComplete = isGameComplete(v_tbl, h_tbl)
					if(gameComplete):
						lastClickedCell = clickedCell #Stores the winning move for game complete effect



		### Screen draw ##

		#Game Complete reveal effect setup
		if(gameComplete):
			if(curRevealOrigin == None): # will run every time a reveal effect ends
				#Reveal Setup

				curRevealOrigin = lastClickedCell
				curRevealDist = 0
				maxRevealDistSqr = len(v_tbl)**2 + len(v_tbl[0])**2 #sets max distance sqr to diagonal sqr

				gameCompleteCounter += 1
				if(gameCompleteCounter > 8):
					gameCompleteCounter = 0

				for i in range(len(v_tbl)):
					for j in range(len(v_tbl[i])):
						v_tbl[i][j] = str(int(gameCompleteCounter))
				
			
		#Reveal Effect
		if(curRevealOrigin != None):
			curRevealDist+=1
			for i in range(len(displayedTable)):
				for j in range(len(displayedTable[i])):## some optimizations could be made for this loop to oly iterate over cells in range
					vect = [i,j]
					vect[0] = curRevealOrigin[0] - vect[0]
					vect[1] = curRevealOrigin[1] - vect[1]
					if(vect[0]**2 + vect[1]**2 <= curRevealDist**2):
						displayedTable[i][j] = v_tbl[i][j]
			if(curRevealDist**2 > maxRevealDistSqr): # stops when maxDistance is reached
				displayedTable = CloneMat(v_tbl)
				curRevealOrigin = None
				curRevealDist = 0


		DrawTable(screen, displayedTable, tiles, tileSpacing)

		
		# pygame display
		pygame.display.update()
		fpsClock.tick(FPS)


	pygame.quit()

if __name__ == "__main__":
	width = max(2,tkinter.simpledialog.askinteger("Table Rows", "Enter the desired width of the minesweeper table."))
	height = max(2,tkinter.simpledialog.askinteger("Table Rows", "Enter the desired height of the minesweeper table."))
	dif = tkinter.simpledialog.askfloat("Difficulty", "Enter the desired difficulty level (0-10).")
	dif = max(min(10, dif), 0)/10

	minBombs = 1
	maxBombs = width*height - 1

	bombs = minBombs + (maxBombs - minBombs) * (dif**2)

	bombs = math.floor(bombs)
	# messagebox.showinfo('Continue','OK')
	MineSweeper(width,height,bombs)
	# MineSweeper(10,10,5)
