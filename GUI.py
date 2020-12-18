from Solver import solveSudoku
from Solver import isSafe
import pygame
import time

# Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH, HEIGHT = 540, 600


# Setting up the display
pygame.init()
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")
FPS = 30
clock = pygame.time.clock()


# Fonts




# Data
#  Cubes, Width, Height, model to check with solution Array, selected row and column, notes

# Methods:
# draw grids and cubes, check if clicked on the gridboard and if yes, return position of it
# Draw in pencil, solidate the pencil, is finished, clearing the selected cell, check if valid and place the value
# Updating the model, toggling between notes on and off

class Grid:
    rows, cols  = 9, 9

    board = [[9,8,0,6,0,0,0,3,1],
             [0,0,7,0,0,0,0,0,0],
             [6,0,0,5,4,0,0,0,0],
             [0,0,0,0,0,8,3,7,4],
             [0,0,0,0,6,0,0,0,0],
             [0,0,0,0,0,0,9,0,2],
             [0,3,2,0,0,7,4,0,0],
             [0,4,0,3,0,0,0,1,0],
             [0,0,0,0,0,0,0,0,0]]

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cubes = [[cube(board[i][j],j,i) for j in range(cols)] for i in range(rows)]


# Data
# pencil Value, Actual Value

# Methods:
# draw(draws a cube and highlights if selected), Set pencil value, set actual value

class Cube:
    def __init__(self,value,row,col):
        self.value = value
        self.pencil = [0,0,0,0,0,0,0,0,0]
        self.selected = False
        self.row = row
        self.col = col


# Draw Time, Mistakes and Notes on and oFF
def drawLeftovers():



def main():
    clock.tick()
    start = time.time()
    board = Grid(540,540)
    key = None
    run = True
    mistakes = 0

    while run:
        
