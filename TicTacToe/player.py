import display
import check

def player_input():
    marker=''
    playermarker={}
    while marker!='X' and marker!='O':
        marker=str(input("Enter Input 'X' or 'O': ")).upper()
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)

def place_marker(board,marker,position):
    board[position]=marker

def player_choice(board):
    display.display_board(board)
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] and not check.space_check(board, position):
        position = 	int(input("Choose position: 1-9"))
    return position