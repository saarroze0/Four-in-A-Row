# import pygame
import numpy as np

def add_pieces(color, column):
    global board,column_free_location
    
    if not(column) in range(7):
        print("not in range")
        return False
        
    if column_free_location[column] < 0:
        print("There is no place in this column")
        return False
    else:
        board[column_free_location[column]][column] = color
        column_free_location[column] -= 1
    return True

def game_play():
    global turnPlayer1 , board
    do=False
    if (turnPlayer1):
        while not(do):
            print("plyer 1 enter piece to the board: ")
            col= int(input())
            do= add_pieces (player1, col)

        turnPlayer1=False
        return winneing(player1)

    else:
        while not(do):
            print("plyer 2 enter piece to the board: ")
            col= int(input())
            do= add_pieces(player2, col)
  
        turnPlayer1=True
        return winneing(player2)
    
def winneing(player):
   
    #vertical
    for c in range(COLUMNS):
        for r in range(ROWS -3):
            if board[r][c]== player and board[r+1][c]== player and board[r+2][c]== player and board[r+3][c]== player:
                return True
    #11
    for c in range(COLUMNS -3):
        for r in range(ROWS -3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True
                
    for c in range(COLUMNS-3):
        for r in range(3,ROWS):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True

    #horizontal
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    return False
 # ==============================================================================================================================================
ROWS = 6
COLUMNS = 7

column_free_location = np.array((5, 5, 5, 5, 5, 5, 5))
board = np.zeros((ROWS, COLUMNS))
player1 = 1
player2 = 2

turnPlayer1 = True
game_over = False
i=0
while i<42 and not game_over:
    print(board)
    if game_play():
        game_over = True
        print(board)
        print("player1 win!!!!") if turnPlayer1 else print("player2 win!!!!") 
    i+=1

if i == 42:
    print(board)
    print("its a tie!!")