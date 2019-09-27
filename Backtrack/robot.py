def okay(board, row, col, res):
    if (0 <= row <= len(board)-1) and (0 <= col <= len(board)-1):
        if (row, col) not in res:
            if (board[row][col] != 1):
                return True
    return False

def find(board, val):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == val:
                return i,j

def move(board, row, col, res, a, b):
    if okay(board, row, col, res):
        res.append((row,col))
        if 3 in (board[row][col+1], board[row+1][col], board[row-1][col], board[row][col-1]):
            res.append((a,b))
            return True
        elif move(board, row, col+1, res, a, b):
            return True
        elif move(board, row+1, col, res, a, b):
            return True
        elif move(board, row-1, col, res, a, b):
            return True
        elif move(board, row, col+1, res, a, b):
            return True
        res.pop()
        board[row][col] = 1
    return False

def print_board(board):
    for i in range(len(board)):
        print(board[i])

board = [[2,0,0,1,1],[0,1,0,3,1],[1,1,0,0,1],[0,0,0,0,1],[1,1,0,0,1]]
print_board(board)
res = []
i,j = find(board, 2)
a,b = find(board, 3)
move(board, i, j, res, a, b)
print(res)





