import pygame
from meta import Meta

class Fonts:
    def __init__(self, height):
        self.height = height
        self.footerFont()
        self.pencilFont()
        self.cubeFont()

    def footerFont(self):
        self.footer_size = int(round(Meta.HEIGHT - self.height)/2)
        self.footer_gap =  int(round(Meta.HEIGHT - self.height)/4)
        self.footer_font = pygame.font.SysFont('comicsans',self.footer_size)
        self.footer_ypos = int(round(self.height + 1.3*self.footer_gap))

    def pencilFont(self):
        self.pencil_font = int(round(self.height/30))
        self.pencil_font = pygame.font.SysFont('comicsans',self.pencil_font)

    def cubeFont(self):
        self.cube_size = round(self.height/15)
        self.cube_font = pygame.font.SysFont('comicsans',self.cube_size)
