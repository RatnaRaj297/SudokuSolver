# Check if the number is repeated in the row
def isSafeRow(board, row, col, num):
    if num in board[row]:
        return False
    return True

# Check if the number is repeated in the column
def isSafeCol(board, row, col, num):
    for i in range(len(board)):
        if board[i][col] == num:
            return False
    return True

# Check if the number is repeated in the box
def isSafeBox(board, row, col, num):
    row = (row//3)*3
    col = (col//3)*3
    for i in range(3):
        for j in range(3):
            if board[row + i][col + j] == num:
                return False
    return True

# Check if it safe to add the number to the board
def isSafe(board, row, col, num):
    return isSafeRow(board, row, col, num) and isSafeCol(board, row, col, num) and isSafeBox(board, row, col, num) and board[row][col]==0


# Finds the first unassigned cell in the board
def findUnassigned(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col] == 0)
                return (row,col)
    return(-1,-1)


def solveSudoku(board):
    # Finds the first unassigned cell in the board
    row, col = findUnassigned(board)

    # The entire sudoku is filled
    if row==-1 and col==-1:
        return True

    # Check for every number
    for num in range(1, 10):
        if isSafe(board, row, col, num):
            board[row][col] = num

            # Success!
            if solveSudoku(board):
                return True;

            # Failure! unmake and try again
            board[row][col] = 0

    # Triggers Backtracking
    return False


board = [[]
         []
         []
         []
         []
         []
         []
         []
         []]

solved_board = [int(x) for line in board for x in line]

if solveSudoku(solved_board):
    print(solved_board)
else:
    print("This Sudoku cannot be solved!")