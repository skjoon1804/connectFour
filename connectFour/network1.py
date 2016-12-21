//  Copyright © 2016 Oh Jun Kwon. All rights reserved.


import connectfour
import socket
from collections import namedtuple
import console
import handle
import both

#pulsar.ics.uci.edu
#5757

ConnectfourConnection = namedtuple('ConnectfourConnection', ['s','s_in', 's_out'])


def network_UI():
    welcome() 
    username = _ask_username()
    host = _ask_host()
    port = _ask_port()
    con = handle.connection(host, port)
    handle.check_connect(con, username)
    
    game = both.init_game()
    while both.continue_game(game):
        #User(red)'s turn
        if (both.player_name(game.turn)) == 'Red':
            print("User(Red)'s turn!")
            move = both.move_decision()
            column = both.column_decision()
            print()        
            update_game = both.operate_move(game, move, column)
            game = update_game

            handle.write_line(con, (move + ' ' + str(column)))


        #Server(yellow)'s turn    
        else:
            feedback = handle.read_line(con)
            #Server makes drop move
            if feedback.startswith("DROP"):
                game = _server_drop(game, feedback)

            #Server makes pop move
            elif feedback.startswith("POP"):
                game = _server_pop(game, feedback)

            #Server returns winner
            elif feedback.startswith("WINNER_YELLOW"):
                print("Server(Yellow) wins!")
                close(con)
            elif feedback.startswith("WINNER_RED"):
                print("User(Red) wins!")
                close(con)
                

    print("Congratulations!", both.player_name(connectfour.winning_player(game)), "wins!")
    handle.close(con)    






def welcome():
    '''print welcome sign and brief explanation when the game is initiated'''
    print("WELCOME to the NETWORK version of CONNECTFOUR!")
    print("☞ User is RED going first. Server is YELLOW going second")
    print()


def _ask_username():
    '''ask for username from user'''
    while True:
        try:
            username = input("Please enter username: ").strip()
            if username =="":
                print("Please specify a username")
                
            elif len(username.split())>=2:
                print("Username cannot contain whitespace")
            else:
                return username
        except:
            print("Please enter a valid username")


def _ask_host():
    '''ask for host info from user'''
    while True:
        host = input("Please enter host: ").strip()
        if host == "":
            print("Please specify a host..name or ip address")        
        else:
            return host


def _ask_port():
    '''ask for port info from user'''
    while True:
        try:
            port = int(input("Please enter port: ").strip())
            if port == "":
                print("Please re-enter an integer between 0 and 65535")
            else:
                return port
        except:
            print("Please re-enter an integer between 0 and 65535")

            
def _server_drop(game,feedback):
    print()
    print("Server(Yellow) is making a move...")
    print()
    try:
        update_game = both.operate_move(game, "DROP", int(feedback[5]))
        game = update_game
        return game
        
    except:
        print("Server gave invalid feedback. Ending the game")
        handle.close(con)

def _server_pop(game, feedback):
    print()
    print("Server(Yellow) is making a move...")
    print()
    try:
        update_game= both.operate_move(game, "POP", int(feedback[4]))
        game = update_game
        return game
        
    except:
        print("Server gave invalid feedback. Ending the game")
        handle.close(con)

    





if __name__ == '__main__':
    network_UI()
