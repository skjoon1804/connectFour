//  Copyright © 2016 Oh Jun Kwon. All rights reserved.

import connectfour


def init_game():
    '''start a fresh board for a new game'''
    new_game = connectfour.new_game_state()
    _create_game_board(new_game.board)       
    return new_game


def continue_game(game):
    '''return TRUE if there is no winner yet'''
    return connectfour.winning_player(game) == connectfour.NONE



def player_name(turn):
    '''translate player info imported from the connectfour library'''
    if turn == 1:
        return "Red"
    elif turn == 2:
        return "Yellow"
    else:
        return "None"
 
def move_decision()->str:
    '''ask user whether to pop or drop'''
    decision = input("[POP] or [DROP]?: ").upper()
    
    if decision == "POP":
        return "POP"

    elif decision == "DROP":
        return "DROP"
    
    else:
        print("Enter a valid command.")
        return move_decision()


def column_decision():
    '''ask user which column to perform action'''
    while True:
        try:
            column = int(input("Please choose a column to make move: "))
        
            if column <= connectfour.BOARD_COLUMNS and column>0:
                return column
            
            else:
                print("Enter a valid column number")
        except:
            print("Enter a valid column number.")

def operate_move(game, move, column):
    '''with move and column info, operate action on the game board'''
    if move == "DROP":
        try:
            new_game = connectfour.drop_piece(game, column-1)
            _create_game_board(new_game.board)
        except:
            print("Enter a valid command")
            new_game = game

        finally:
            return new_game
    
    elif move == "POP":
        try:
            new_game = connectfour.pop_piece(game, column-1)
            _create_game_board(new_game.board)

        except:
            print("Enter a valid command")
            new_game = game
            
        finally:
            return new_game






def _create_game_board(board):
    '''update and generate gameboard on to the shell'''
    title= ""
    for count in range(connectfour.BOARD_COLUMNS):
        title = title + str(count + 1) + '  '
    print(title)
    for row in range(connectfour.BOARD_ROWS):
        for column in range(connectfour.BOARD_COLUMNS):
            if board[column][row] == 0:
                print(".", end='  ')
            elif board[column][row] == 1:
                print("R", end='  ')
            elif board[column][row] == 2:
                print("Y", end='  ')
                    
        print(" ")


