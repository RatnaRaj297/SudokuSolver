import Solver
import pygame

fps = 60

def visualize(board, win, fonts, play_time, clock):

    def solveSudoku(board):
        clock.tick(fps)
        find = Solver.findUnassigned(board.model)
        if not find:
            return True
        else:
            row, col = find
        # Select to Show Selection
        board.clearCubesSelection()
        board.cubes[row][col].setSelected()
        board.selected_cube = (row, col)

        # check for every numbers
        for num in range(1,10):
            selected_cube = (row,col)
            if Solver.isSafe(board.model, row, col, num):
                board.cubes[row][col].value = num
                board.cubes[row][col].is_green = True
                board.cubes[row][col].is_correct = True
                board.updateModel()
                board.draw(win,fonts,play_time)
                pygame.time.wait(500)


                if solveSudoku(board):
                    return True

                # Failure!
                board.cubes[row][col].is_correct = False
                board.updateModel()
                board.draw(win,fonts,play_time)
                pygame.time.wait(500)
                board.delete()
                board.updateModel()

        return False

    solveSudoku(board)
    print("Game Over")
    board.clearCubesSelection()
