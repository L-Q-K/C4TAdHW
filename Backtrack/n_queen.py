board_out = [0,0,0,0]

def is_safe(board,row,col):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                if (i == row) or (j == col):
                    return False
                if abs(i-row) - abs(j-col) == 0:
                    return False
    return True

def arr_queen(board,row):
    if row == len(board):
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if arr_queen(board,row + 1):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    for i in range(len(board)):
        print(board[i])

board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
arr_queen(board,0)
print_board(board)

res = []
res.append((2,3))
print(res[0][1])