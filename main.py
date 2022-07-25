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



def add_pieces_AI(tempBoard, color, column):
    # global board,column_free
    # board=tempBoard.copy()
        
    if column_free[column] < 0:
        return tempBoard
    else:
        tempBoard[column_free[column]][column] = color
        column_free[column] -= 1
    return board

def game_play():
    global turnPlayer , board, column_free_location
    do=False
    if (turnPlayer):
        while not(do):
            print("plyer 1 enter piece to the board: ")
            col= int(input())
            do= add_pieces (player1, col)

        turnPlayer=False
        return winneing(board,player1)

    else:
        temp_board = board.copy()
        temp_column_free = column_free_location.copy()
        col = miniMaxTree(temp_board, temp_column_free, 5, np.inf, -np.inf, 2)
        
        # print(column_free)
        add_pieces (player2, col)
        turnPlayer=True
        return winneing(board,player2)
        # while not(do):
        #     print("plyer 2 enter piece to the board: ")
        #     col= int(input())
        #     do= add_pieces (player2, col)

        # turnPlayer=True
        # return winneing(board,player2)

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
            arr[0]=board[r][c]
            arr[1]=board[r+1][c]
            arr[2]=board[r+2][c]
            arr[3]=board[r+3][c]
            heuristics += positionScore(arr,player)

    #diagonal 
    for c in range(COLUMNS -3):
        for r in range(ROWS -3):
            arr[0]=board[r][c]
            arr[1]=board[r+1][c+1]
            arr[2]=board[r+2][c+2]
            arr[3]=board[r+3][c+3]
            heuristics += positionScore(arr,player)

    for c in range(COLUMNS-3):
        for r in range(3,ROWS):
            arr[0]=board[r][c]
            arr[1]=board[r-1][c+1]
            arr[2]=board[r-2][c+2]
            arr[3]=board[r-3][c+3]
            heuristics += positionScore(arr,player)
         
    #horizontal
    for c in range(COLUMNS-3):
        for r in range(ROWS):
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


def miniMaxTree(board,column_free_location,depth,a,b,player):
    column_free1= column_free_f(column_free_location)
    is_terminal = is_terminal_node(board, column_free_location)
    print(is_terminal) 
    if (depth == 0 or is_terminal):
	    if (is_terminal):
			if winneing(board, player2):
				return (None, 100000000000000)
			elif winneing(board, player1):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, CalculationOfHeuristics(board, player2))
        
        if player==player2:
            return 0
    
    
    
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
ROWS = 6
COLUMNS = 7

column_free_location = np.array((5, 5, 5, 5, 5, 5, 5))
# ?olumn_free = np.array((4, 55, -65, np.inf, 51, np.nan, 5))

board = np.zeros((ROWS, COLUMNS))
player1 = 1
player2 = 2
# board[5][0]= 1
# board[3][2]= 0
# board[4][3]= 0
# board[4][2]= 0
# board[5][2]= 1
# board[5][3]= 2
# print(board)
# print( CalculationOfHeuristics(board,2))


turnPlayer = True
game_over = False
i=0
#print(miniMaxTree(board,0))
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