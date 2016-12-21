//  Copyright © 2016 Oh Jun Kwon. All rights reserved.

import connectfour
import both



def console_UI():

    welcome()
    game = both.init_game()
    while both.continue_game(game):    
        print(both.player_name(game.turn)+" player's turn.")     
        move = both.move_decision()
        column = both.column_decision()
        print()
        update_game = both.operate_move(game, move, column)
        game = update_game
  
    print("Congratulations!", both.player_name(connectfour.winning_player(game)), "player wins")




def welcome():
    '''print welcome sign when the game is initiated'''
    print("WELCOME to the console-only version of CONNECTFOUR!")
    print()



    








if __name__ == '__main__':
    console_UI()

