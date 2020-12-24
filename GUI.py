from Solver import solveSudoku, isSafe
from Solver import isSafe
from grid import Grid
from fonts import Fonts
from meta import Meta
from visualizer import visualize
import pygame
import time


# Setting up the display
pygame.init()
win = pygame.display.set_mode((Meta.WIDTH, Meta.HEIGHT))
pygame.display.set_caption("Sudoku")
FPS = 60
clock = pygame.time.Clock()


def main():
    start = time.time()
    board = Grid(Meta.board_height,Meta.board_width)
    fonts = Fonts(Meta.board_height)
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
                board.click(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                elif event.key == pygame.K_2:
                    key = 2
                elif event.key == pygame.K_3:
                    key = 3
                elif event.key == pygame.K_4:
                    key = 4
                elif event.key == pygame.K_5:
                    key = 5
                elif event.key == pygame.K_6:
                    key = 6
                elif event.key == pygame.K_7:
                    key = 7
                elif event.key == pygame.K_8:
                    key = 8
                elif event.key == pygame.K_9:
                    key = 9
                else:
                    key = None
                board.place(key)
                if board.isFinished():
                    print("Game Over")
                    run = False

                if event.key == pygame.K_DELETE:
                    board.delete()

                if event.key == pygame.K_SPACE:
                    visualize(board, win, fonts, play_time, clock)
                    run = False



        board.draw(win, fonts, play_time)


main()
pygame.quit()
