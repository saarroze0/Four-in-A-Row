import pygame
import numpy as np

def add_pieces_player(color, column):
    global board
    tempBoard=board.copy()
    
    if not(column) in range(7):
        print("not in range")
        return [False, tempBoard]
        
    if column_free_location[column] < 0:
        print("There is no place in this column")
        return [False, tempBoard]
    else:
        tempBoard[column_free_location[column]][column] = color
        column_free_location[column] -= 1
    return [True, tempBoard]

def add_pieces_AI(color, column):
    global board,column_free
    tempBoard=board.copy()
        
    if column_free[column] < 0:
        return [False, tempBoard]
    else:
        tempBoard[column_free[column]][column] = color
        column_free[column] -= 1
    return [True, tempBoard]

def game_play():
    global turnPlayer , board, column_free
    do=False
    if (turnPlayer):
        while not(do):
            print("plyer enter piece to the board: ")
            col = int(input())
            answer = add_pieces_player (player1, col)
            do = True #answer[0]
        turnPlayer=False
        return answer[1]

    else:
        column_free = column_free_location.copy
        print (column_free)
        miniMaxTree(board,0)
        # while not(do):
        #     # print("plyer 2 enter piece to the board: ")
        #     col= int(input())
        #     answer = add_pieces_player (player2, col)
        #     do = answer[0]
        # turnPlayer=True
        # return answer[1]


def CalculationOfHeuristics(board):
    return 0

def miniMaxTree(board,i):
    arr =np.array((0,0,0,0,0,0,0))
    if(i<5):
        if(i%2==0):
            for x in range(7):
                arr[x]=miniMaxTree(add_pieces_AI(1,x)[1],i+1)
        else:
            for x in range(7):
                arr[x]=miniMaxTree(add_pieces_AI(2,x)[1],i+1)
    else:
        return CalculationOfHeuristics(board)

    if(i%2==0):
        return np.max(arr)
    else:
        return np.min(arr)
    

    
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
column_free = np.array((4, 55, -65, np.inf, 51, np.nan, 5))
# print(np.nan+8)
# print(np.min(column_free))
board = np.zeros((ROWS, COLUMNS))
player1 = 1
player2 = 2

turnPlayer = True
game_over = False
i=0
# print(miniMaxTree(board,0))
while i<42 and not game_over:
    print(board)
    if game_play():
        game_over = True
        print(board)
        print("player1 win!!!!") if turnPlayer else print("player2 win!!!!") 
    i+=1

if i == 42:
    print(board)
    print("its a tie!!")