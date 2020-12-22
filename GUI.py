from Solver import solveSudoku
from Solver import isSafe
import pygame
import time

# Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (112, 127, 128)
RED = (255,0,0)
LIGHT_BLUE = (187, 222, 251)
BLUE = (74,144,226)
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
        # self.pencilFont()
        self.cubeFont()

    def footerFont(self):
        self.footer_size = int(round(HEIGHT - self.height)/2)
        self.footer_gap =  int(round(HEIGHT - self.height)/4)
        self.footer_font = pygame.font.SysFont('comicsans',self.footer_size)
        self.footer_ypos = int(round(self.height + 1.3*self.footer_gap))

    # def pencilFont(self):

    def cubeFont(self):
        self.cube_size = round(self.height/15)
        self.cube_font = pygame.font.SysFont('comicsans',self.cube_size)

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
        self.offset = offset
        self.gap = (self.height - 2*self.offset)/ 9
        self.cubes = [[Cube(self.board[i][j],j,i,self.gap,self.offset) for j in range(9)] for i in range(9)]
        self.notes = False

    def updateModel(self):
        self.model = [[cube.value for cube in line] for line in self.cubes]

    def draw(self, win, fonts, play_time):
        win.fill(WHITE)

        # Gridlines
        for i in range(10):
            thickness = 1
            color = GREY
            if i%3 == 0:
                color = BLACK
                thickness = 2
            pygame.draw.line(win, color, (self.offset + 0, self.gap*i), (self.offset+ self.width, self.gap*i), thickness)
            pygame.draw.line(win, color, (self.offset + self.gap*i, 0), (self.offset + self.gap*i, self.height), thickness)

        # Numbers
        for line in self.cubes:
            for cube in line:
                cube.draw(win, fonts, self)

        # NOTES
        def drawNotes(message):
            text1 = fonts.footer_font.render("Notes: ", 1, BLACK)
            win.blit(text1, (15, fonts.footer_ypos))

            color = GREY
            if message == "ON":
                color = BLUE
            text2 = fonts.footer_font.render(message, 1, WHITE)

            # Coordinates of the rectangle
            left = 17 + text1.get_width()
            top = self.height + (HEIGHT-(self.height))/5
            rect_width =  text2.get_width() + 20
            rect_height = ((HEIGHT-(self.height))*3)/5 - 2

            self.rect = (left, top, rect_width, rect_height)
            pygame.draw.rect(win, color, pygame.Rect(self.rect))
            win.blit(text2, (10 + left, fonts.footer_ypos))

        if self.notes:
            drawNotes("ON")
        else:
            drawNotes("OFF")

        # Time
        time = formatTime(play_time)
        text = fonts.footer_font.render("Time: " + time, 1, BLACK)
        win.blit(text, (WIDTH-text.get_width()-15,fonts.footer_ypos))

        pygame.display.update()



    def click(self, pos):
        # clcked on a sudoku cell
        if self.offset<pos[0] and pos[0]<(self.width + self.offset) and pos[1]<self.height:
            col_no = int((pos[0] - self.offset)//self.gap)
            row_no = int(pos[1]//self.gap)
            print(row_no,col_no)
            for line in self.cubes:
                for cube in line:
                    cube.selected = False
            self.cubes[row_no][col_no].setSelected()
            return (row_no,col_no)

         # Clicked on notes
        if self.rect[0]<pos[0] and self.rect[1]<pos[1] and pos[0]<self.rect[0]+self.rect[2] and pos[1]<self.rect[1]+self.rect[3]:
            self.notes = ~(self.notes)

        return None


# Data
# pencil Value, Actual Value

# Methods:
# draw(draws a cube and highlights if selected), Set pencil value, set actual value

class Cube:
    def __init__(self, value, row, col, gap, offset):
        self.value = value
        self.temp = 0
        self.pencil = [0,0,0,0,0,0,0,0,0]
        self.selected = False
        self.row = row
        self.col = col
        self.gap = gap
        self.offset = offset
        self.col_pos = self.offset + self.col*self.gap
        self.row_pos = self.row*self.gap

        row_thickness = 1
        col_thickness = 1
        if self.row%3 == 0:
            row_thickness = 3
        if self.col%3 == 0:
            col_thickness = 3

        self.rect = (self.row_pos + row_thickness,self.col_pos+col_thickness, self.gap-row_thickness,self.gap-col_thickness)

    def setSelected(self):
        if self.value!=0:
            self.selected = False
        else:
            self.selected = True

    def draw(self, win, fonts, board):

        # If the cell is selected
        if self.selected:
            pygame.draw.rect(win, LIGHT_BLUE, pygame.Rect(self.rect))

        # MAIN TEXT
        if self.temp !=0 or self.value!=0:
            if self.value != 0:
                text = fonts.cube_font.render(str(self.value), 1, BLACK)
            else:
                text = fonts.cube_font.render(str(self.temp), 1, RED)
            x_font = self.row_pos + (self.gap - text.get_width())/2
            y_font = self.col_pos + (self.gap - text.get_height())/2
            win.blit(text, (x_font,y_font))




def formatTime(secs):
    sec = (int(secs))%60
    minute = int(secs//60)%60
    hour = minute//60
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)

        board.draw(win, fonts, play_time)






main()
pygame.quit()
