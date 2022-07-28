from ast import Return
import math
import random
from re import T
import pygame
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
    global turnPlayer , board, column_free_location
    do=False
    inPut= True
    if (turnPlayer):
        while not(do):
            print("player 1 enter piece to the board: ")
            while inPut:
                try:
                    col= int(input())
                    inPut =False
                except:
                    print ("wrong input!! enter a number")

            do= add_pieces (player1, col)

        turnPlayer=False
        return winneing(board,player1)

    else:
        temp_board = board.copy()
        temp_column_free = column_free_location.copy()
        col = miniMaxTree(temp_board, temp_column_free, 5, -np.inf, np.inf)[0]
        print("AI enter a piece to " + str(col))

        add_pieces (player2, col)
        turnPlayer=True
        return winneing(board,player2)
       

def positionScore (arr,player):
    if ((player1 in arr and player2 in arr )or (arr.count(0)==4)):
        return 0

    num = 4-arr.count(0)
    match num:
        case 1:
            score=1
        case 2:
            score=5
        case 3:
            score=10
        case 4:
            score=100
    
    if (player in arr):
        return score
    else:
        return score * -1
    
def CalculationOfHeuristics(board,player):
    heuristics = 0
    arr =[0,0,0,0]
    #vertical
    for c in range(COLUMNS):
        for r in range(ROWS -3):
            arr =[0,0,0,0]
            arr[0]=board[r][c]
            arr[1]=board[r+1][c]
            arr[2]=board[r+2][c]
            arr[3]=board[r+3][c]
            heuristics += positionScore(arr,player)

    #diagonal 
    for c in range(COLUMNS -3):
        for r in range(ROWS -3):
            arr =[0,0,0,0]
            arr[0]=board[r][c]
            arr[1]=board[r+1][c+1]
            arr[2]=board[r+2][c+2]
            arr[3]=board[r+3][c+3]
            heuristics += positionScore(arr,player)

    for c in range(COLUMNS-3):
        for r in range(3,ROWS):
            arr =[0,0,0,0]
            arr[0]=board[r][c]
            arr[1]=board[r-1][c+1]
            arr[2]=board[r-2][c+2]
            arr[3]=board[r-3][c+3]
            heuristics += positionScore(arr,player)
         
    #horizontal
    for c in range(COLUMNS-3):
        for r in range(ROWS):
            arr =[0,0,0,0]
            arr[0]=board[r][c]
            arr[1]=board[r][c+1]
            arr[2]=board[r][c+2]
            arr[3]=board[r][c+3]
            heuristics += positionScore(arr,player)


    return heuristics

def column_free_f(arr):
    temp =[]
    for i in range(7):
        if arr[i]>=0:
            temp.append(i)
    return temp

def is_terminal_node(board, column_free_location):
	return winneing(board, player1) or winneing(board, player2) or len(column_free_f(column_free_location)) == 0


def miniMaxTree(board,column_free_location,depth,a,b):
    column_free1= column_free_f(column_free_location)
    is_terminal = is_terminal_node(board, column_free_location)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winneing(board, player2):
                return (None, math.inf)
            elif winneing(board, player1):
                return (None, -math.inf)
        else:
                # print(board)
                return (None,CalculationOfHeuristics(board,player2))
    if depth%2==1:
        temp_board=board.copy()
        temp_column_free_location=column_free_location.copy()
        value = -math.inf
        column = random.choice(column_free1)
        for col in column_free1:
            row= temp_column_free_location[col]
            temp_column_free_location[col] -= 1
            temp_board[row][col] = player2
            new_score = miniMaxTree(temp_board, temp_column_free_location, depth-1, a, b)[1]
            temp_column_free_location[col] += 1
            temp_board[row][col] = 0
            if new_score > value:
                value= new_score
                column=col
            a = max(a, value)
            if a >= b:
                break
        return column, value
    else:
        temp_board=board.copy()
        temp_column_free_location=column_free_location.copy()
        value = math.inf
        column = random.choice(column_free1)
        for col in column_free1:
            row= temp_column_free_location[col]
            temp_column_free_location[col] -= 1
            temp_board[row][col] = player1
            new_score = miniMaxTree(temp_board, temp_column_free_location, depth-1, a, b)[1]
            temp_column_free_location[col] += 1
            temp_board[row][col] = 0
            if new_score < value:
                value = new_score
                column = col
            b = min(b, value)
            if a >= b:
                break
        return column, value
    
    
    
def winneing(board,player):
   
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
# ==============================================================================================================================================
ROWS = 6
COLUMNS = 7

column_free_location = np.array((5, 5, 5, 5, 5, 5, 5))

board = np.zeros((ROWS, COLUMNS))
player1 = 1
player2 = 2

turnPlayer = True
game_over = False
i=0

while i<42 and not game_over:
    print(" "+str([0,1,2,3,4,5,6]))
    print(board)
    print()
    if game_play():
        game_over = True
        print(board)
        print("player1 win!!!!") if not turnPlayer else print("AI win!!!!") 
    i+=1

if i == 42:
    print(board)
    print("its a tie!!")