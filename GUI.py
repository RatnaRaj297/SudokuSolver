from Solver import solveSudoku
from Solver import isSafe
import pygame
import time

# Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (112, 127, 128)
WIDTH, HEIGHT = 542, 600


# Setting up the display
pygame.init()
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sudoku")
FPS = 60
clock = pygame.time.Clock()


# Fonts
class Fonts:
    def __init__(self, height):
        self.height = height
        self.footerFont()

    def footerFont(self):
        self.footer_size = int(round(HEIGHT - self.height)/2)
        self.footer_gap =  int(round(HEIGHT - self.height)/4)
        print(self.footer_size )
        self.footer_font = pygame.font.SysFont('comicsans',self.footer_size)
        self.footer_ypos = int(round(self.height + 1.3*self.footer_gap))

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

    def __init__(self, width, height, offset):
        self.height = height
        self.width = width
        self.cubes = [[Cube(self.board[i][j],j,i) for j in range(9)] for i in range(9)]
        self.offset = offset
        self.notes = False

    def updateModel(self):
        self.model = [[cube.value for cube in line] for line in self.cubes]

    def draw(self, win):
        win.fill(WHITE)
        gap = (self.height - 2*self.offset)/ 9

        for i in range(10):
            thickness = 1
            color = GREY
            if i%3 == 0:
                color = BLACK
                thickness = 2
            pygame.draw.line(win, color, (self.offset + 0, gap*i), (self.offset+ self.height, gap*i), thickness)
            pygame.draw.line(win, color, (self.offset + gap*i, 0), (self.offset + gap*i, self.width), thickness)

        pygame.display.update()





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
def drawLeftovers(win, fonts, play_time):
    time = formatTime(play_time)

    # Time
    text = fonts.footer_font.render("Time: " + time, 1, BLACK)
    win.blit(text, (WIDTH-text.get_width()-15,fonts.footer_ypos))
    pygame.display.update()


def formatTime(secs):
    sec = int(secs)%60
    minute = int((secs//60)%60)
    hour = int(secs//(60*60))

    time  = " " + str(minute) + ":" +  str(sec)
    return time

def main():

    start = time.time()
    board = Grid(540,540,0)
    fonts = Fonts(540)
    key = None
    run = True
    mistakes = 0

    while run:
        clock.tick(FPS)
        play_time = time.time() - start

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        board.draw(win)
        drawLeftovers(win, fonts, play_time)

    return start



main()
pygame.quit()
