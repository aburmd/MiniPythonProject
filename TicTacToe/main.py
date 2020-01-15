import replay
import check
import win
import player
import display

def playTicTac():
    while True:
        print('Welcome to Tic Tac Toe!')
        board=['']*10
        player1,player2=player.player_input()
        marker=player1
        match_completed=False
        while not check.full_board_check(board):
            print('marker:{}'.format(marker))
            position=player.player_choice(board)
            player.place_marker(board,marker,position)
            if win.win_check(board, marker):
                print('{} player wins!'.format(marker))
                match_completed=True
                display.display_board(board)
                break
            if marker==player1:
                marker=player2
            else:
                marker=player1
        if not match_completed:
            print('Match Tie!!!')
            display.display_board(board)
        if not replay.replay():
            break

playTicTac()