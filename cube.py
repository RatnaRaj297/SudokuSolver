from fonts import Fonts
import pygame
from meta import colors

class Cube:
    def __init__(self, value, row, col, gap):
        self.value = value
        self.is_correct = True
        self.pencil = [[False,False,False],[False,False,False],[False,False,False]]
        self.selected = False
        self.is_green = False
        self.row = row
        self.col = col
        self.gap = gap
        self.pencil_gap = gap/3
        self.x_pos = self.col*self.gap
        self.y_pos = self.row*self.gap

        y_thickness = 1
        x_thickness = 1
        if self.row%3 == 0:
            y_thickness = 3
        if self.col%3 == 0:
            x_thickness = 3

        # The rectangle object specifying the location for each individual cube
        self.rect = (self.x_pos + x_thickness, self.y_pos + y_thickness, self.gap-x_thickness,self.gap-y_thickness)


    # Selects the cell only if the true value has not been input yet
    def setSelected(self):
        if self.value!=0 and self.is_correct:
            self.selected = False
        else:
            self.selected = True


    # Draw the cell details
    def draw(self, win, fonts):
        # To distuinguish correct input cells from the intitial cells and also helps in visualization algorithm
        if self.is_green:
            pygame.draw.rect(win, colors.GREEN, pygame.Rect(self.rect))

        # If the value in the cell is wrong
        if self.is_correct is False:
            pygame.draw.rect(win, colors.LIGHT_RED, pygame.Rect(self.rect))

        # If the cell is selected
        if self.selected:
            pygame.draw.rect(win, colors.LIGHT_BLUE, pygame.Rect(self.rect))


        # Pencil Text
        if self.value == 0:
            for i in range(3):
                for j in range(3):
                    if self.pencil[i][j]:
                        text = fonts.pencil_font.render(str(3*i + j + 1), 1, colors.GREY)
                        x_font = round(self.x_pos + j*self.pencil_gap + (self.pencil_gap - text.get_width())/2)
                        y_font = round(self.y_pos + i*self.pencil_gap + (self.pencil_gap - text.get_height())/2)
                        win.blit(text, (x_font, y_font))
        # MAIN TEXT
        else:
            color = colors.BLACK
            if self.is_correct is False:
                color = colors.RED
            text = fonts.cube_font.render(str(self.value), 1, color)
            x_font = self.x_pos + (self.gap - text.get_width())/2
            y_font = self.y_pos + (self.gap - text.get_height())/2
            win.blit(text, (x_font,y_font))
