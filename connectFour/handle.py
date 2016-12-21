//  Copyright © 2016 Oh Jun Kwon. All rights reserved.

import socket
from collections import namedtuple


ConnectfourConnection = namedtuple('ConnectfourConnection', ['s','s_in', 's_out'])

class ConnectfourError(Exception):
    pass
        

def connection(host, port):
    '''make connection with the server, quit if failed'''
    try:
        s = socket.socket()
        s.connect((host, port))
        s_in = s.makefile('r')
        s_out = s.makefile('w')
 
        return ConnectfourConnection(s, s_in, s_out)

    except:
        #raise ConnectfourError()
        print("Connection failed!")
        quit()
        
        

def check_connect(con, username):
    '''initiate network based game by sending and receiving certain strings'''
    try:
        _hello(con, username)
        _ai_game(con)
    except:
        print("Connection failed!")
        quit()






def _hello(con, username):
    '''send username info and wait for response'''
    write_line(con, "I32CFSP_HELLO " + username)
    _expect_line(con, "WELCOME " + username)

def _ai_game(con):
    '''send signal that we want to play game and wait for response'''
    write_line(con, "AI_GAME")
    _expect_line(con, "READY")


def write_line(con, line):
    '''send desired lines to the server'''
    con.s_out.write(line + '\r\n')
    con.s_out.flush()


def _expect_line(con, expected_line):
    '''expect desired lines from the server'''
    line = read_line(con)
    if expected_line != line:
        #raise ConnectfourError()
        print("Connection failed!")
        quit()

def read_line(con):
    '''read lines received from the server'''
    return con.s_in.readline().strip()

def close(con):
    '''close connection with the server'''
    con.s_in.close()
    con.s_out.close()
    con.s.close()
