from Solver import isSafe, solveSudoku
from fonts import Fonts
from meta import colors
from meta import Meta
from cube import Cube
import pygame



class Grid:

    board = [[9,8,0,6,0,0,0,3,1],
             [0,0,7,0,0,0,0,0,0],
             [6,0,0,5,4,0,0,0,0],
             [0,0,0,0,0,8,3,7,4],
             [0,0,0,0,6,0,0,0,0],
             [0,0,0,0,0,0,9,0,2],
             [0,3,2,0,0,7,4,0,0],
             [0,4,0,3,0,0,0,1,0],
             [0,0,0,0,0,0,0,0,0]]

            # [9, 8, 4, 6, 7, 2, 5, 3, 1]
            # [2, 5, 7, 8, 3, 1, 6, 4, 9]
            # [6, 1, 3, 5, 4, 9, 8, 2, 7]
            # [5, 6, 1, 9, 2, 8, 3, 7, 4]
            # [4, 2, 9, 7, 6, 3, 1, 8, 5]
            # [3, 7, 8, 4, 1, 5, 9, 6, 2]
            # [8, 3, 2, 1, 5, 7, 4, 9, 6]
            # [7, 4, 5, 3, 9, 6, 2, 1, 8]
            # [1, 9, 6, 2, 8, 4, 7, 5, 3]


    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.gap = (self.width)/ 9
        self.cubes = [[Cube(self.board[i][j],i,j,self.gap) for j in range(9)] for i in range(9)]
        self.notes = False
        self.selected_cube = None
        self.updateModel()

    def updateModel(self):
        self.model = [[cube.value if cube.is_correct else 0 for cube in line] for line in self.cubes]

    # Draw the entire board
    def draw(self, win, fonts, play_time):
        win.fill(colors.WHITE)

        # Gridlines
        for i in range(10):
            thickness = 1
            color = colors.GREY
            if i%3 == 0:
                color = colors.BLACK
                thickness = 2
            pygame.draw.line(win, color, (0, self.gap*i), (self.width, self.gap*i), thickness)
            pygame.draw.line(win, color, (self.gap*i, 0), (self.gap*i, self.height), thickness)

        # Individual cube's numbers
        for line in self.cubes:
            for cube in line:
                cube.draw(win, fonts)

        # NOTES
        def drawNotes(message):
            text1 = fonts.footer_font.render("Notes: ", 1, colors.BLACK)
            win.blit(text1, (15, fonts.footer_ypos))

            color = colors.GREY
            if message == "ON":
                color = colors.BLUE
            text2 = fonts.footer_font.render(message, 1, colors.WHITE)

            # Coordinates of the rectangle
            left = 17 + text1.get_width()
            top = self.height + (Meta.HEIGHT-(self.height))/5
            rect_width =  text2.get_width() + 20
            rect_height = ((Meta.HEIGHT-(self.height))*3)/5 - 2

            self.rect = (left, top, rect_width, rect_height)
            pygame.draw.rect(win, color, pygame.Rect(self.rect))
            win.blit(text2, (10 + left, fonts.footer_ypos))

        if self.notes:
            drawNotes("ON")
        else:
            drawNotes("OFF")


        # Time
        time = formatTime(play_time)
        text = fonts.footer_font.render("Time: " + time, 1, colors.BLACK)
        win.blit(text, (Meta.WIDTH-text.get_width()-15,fonts.footer_ypos))

        pygame.display.update()

    # Clearing the cubes selection
    def clearCubesSelection(self):
        for line in self.cubes:
            for cube in line:
                cube.selected = False
        self.selected_cube = None

    # Where was the mouse clicked
    def click(self, pos):
        # clcked on a sudoku cell
        if 0<pos[0] and pos[0]<(self.width) and pos[1]<self.height:
            col_no = int(pos[0]//self.gap)
            row_no = int(pos[1]//self.gap)

            # if the cube can be selected
            if  ~self.cubes[row_no][col_no].is_correct or self.cubes[row_no][col_no].value!=0:
                self.clearCubesSelection()
                self.cubes[row_no][col_no].setSelected()
                self.selected_cube = (row_no, col_no)

        # Clicked on notes
        elif self.rect[0]<pos[0] and self.rect[1]<pos[1] and pos[0]<self.rect[0]+self.rect[2] and pos[1]<self.rect[1]+self.rect[3]:
            self.notes = ~(self.notes)

        # Clicked elsewhere
        else:
            self.clearCubesSelection()


    # Place the clicked key
    def place(self, key):
        if key is not None and self.selected_cube is not None :
            row, col = self.selected_cube
            # If notes is off
            if not self.notes:
                self.cubes[row][col].value = key
                unupdated_model = self.model
                self.updateModel()
                if isSafe(unupdated_model, row, col, key) and solveSudoku(self.model):
                    self.cubes[row][col].is_correct = True
                    self.cubes[row][col].is_green = True
                    self.clearCubesSelection()
                else:
                    self.cubes[row][col].is_correct = False
                self.updateModel()
            # Notes are off
            else:
                self.cubes[row][col].pencil[int((key-1)//3)][int((key-1)%3)] = ~self.cubes[row][col].pencil[int((key-1)//3)][int((key-1)%3)]

    def delete(self):
        if self.selected_cube is not None:
            row, col = self.selected_cube
            self.cubes[row][col].is_green = False 
            if self.cubes[row][col].is_correct is False:
                self.cubes[row][col].value = 0
                self.cubes[row][col].is_correct = True



    def isFinished(self):
        is_finished = True
        for line in self.model:
            for cell in line:
                if cell==0:
                    is_finished = False
        return is_finished


def formatTime(secs):
    sec = (int(secs))%60
    minute = int(secs//60)%60
    hour = minute//60
    time  = " " + str(minute) + ":" +  str(sec)
    return time
