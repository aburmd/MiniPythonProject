
def win_check(board, mark):
    if horizontal_check(board,mark) or vertical_check(board,mark) or diagonal_check(board,mark):
        return True

def horizontal_check(board,mark):
    x,y,z=1,4,7
    for i in x,y,z:
        if board[i]==board[i+1] and board[i]==board[i+2] and board[i]==mark:
            return True

def vertical_check(board,mark):
    x,y,z=1,2,3
    for i in x,y,z:
        if board[i]==board[i+3] and board[i]==board[i+6] and board[i]==mark:
            return True

def diagonal_check(board,mark):
    if board[5]==board[1] and board[5]==board[9] and board[5]==mark:
        return True
    elif board[5]==board[3] and board[5]==board[7] and board[5]==mark:
        return True