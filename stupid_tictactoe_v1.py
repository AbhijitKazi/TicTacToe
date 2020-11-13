# Tic Tac Toe
# User Input is required
# You can NEVER WIN THIS GAME :D :D
import numpy as np
import random
from time import sleep

# Creating Board
def create_board():
    return(np.array([[0,0,0],
                     [0,0,0],
                     [0,0,0]]))
    
# Placing Player's Position
def player_move(board, player_pos):
    if player_pos == 1:
        if board[0, 0] != 0:
            print("Wrong Input")
        else:
            board[0, 0] = 1
        
    elif player_pos == 2:
        if board[0, 1] != 0:
            print("Wrong Input")
        else:
            board[0, 1] = 1
        
    elif player_pos == 3:
        if board[0, 2] != 0:
            print("Wrong Input")
        else:
            board[0, 2] = 1
        
    elif player_pos == 4:
        if board[1, 0] != 0:
            print("Wrong Input")
        else:
            board[1, 0] = 1
        
    elif player_pos == 5:
        if board[1, 1] != 0:
            print("Wrong Input")
        else:
            board[1, 1] = 1
        
    elif player_pos == 6:
        if board[1, 2] != 0:
            print("Wrong Input")
        else:
            board[1, 2] = 1
        
    elif player_pos == 7:
        if board[2, 0] != 0:
            print("Wrong Input")
        else:
            board[2, 0] = 1
        
    elif player_pos == 8:
        if board[2, 1] != 0:
            print("Wrong Input")
        else:
            board[2, 1] = 1
        
    elif player_pos == 9:
        if board[2, 2] != 0:
            print("Wrong Input")
        else:
            board[2, 2] = 1
    
    return(board)

# Move One
def move_one(board):
    if board[0][1] == 0:
        board[0][1] = 2
    elif board[0][2] == 0:
        board[0][2] = 2
    elif board[1][1] == 0:
        board[1][1] = 2
    elif board[2][2] == 0:
        board[2][2] = 2
    elif board[1][0] == 0:
        board[1][0] = 2
    elif board[2][0] == 0:
        board[2][0] = 2
    return(board)

# Move Two
def move_two(board):
    if board[0][0] == 0:
        board[0][0] = 2
    elif board[0][2] == 0:
        board[0][2] = 2
    elif board[1][1] == 0:
        board[1][1] = 2
    elif board[2][1] == 0:
        board[2][1] = 2
    elif board[1][0] == 0:
        board[1][0] = 2
    elif board[1][2] == 0:
        board[1][2] = 2
    return(board)

# Move Three
def move_three(board):
    if board[0][0] == 0:
        board[0][0] = 2
    elif board[0][1] == 0:
        board[0][1] = 2
    elif board[1][1] == 0:
        board[1][1] = 2
    elif board[2][0] == 0:
        board[2][0] = 2
    elif board[1][2] == 0:
        board[1][2] = 2
    elif board[2][2] == 0:
        board[2][2] = 2
    return(board)

# Move Four
def move_four(board):
    if board[0][0] == 0:
        board[0][0] = 2
    elif board[0][1] == 0:
        board[0][1] = 2
    elif board[1][1] == 0:
        board[1][1] = 2
    elif board[1][2] == 0:
        board[1][2] = 2
    elif board[2][0] == 0:
        board[2][0] = 2
    elif board[2][1] == 0:
        board[2][1] = 2
    return(board)

# Move Five
def move_five(board):
    if board[0][0] == 0:
        board[0][0] = 2
    elif board[0][1] == 0:
        board[0][1] = 2
    elif board[0][2] == 0:
        board[0][2] = 2
    elif board[1][0] == 0:
        board[1][0] = 2
    elif board[1][2] == 0:
        board[1][2] = 2
    elif board[2][0] == 0:
        board[2][0] = 2
    elif board[2][1] == 0:
        board[2][1] = 2
    elif board[2][2] == 0:
        board[2][2] = 2
    return(board)

# Move Six
def move_six(board):
    if board[0][1] == 0:
        board[0][1] = 2
    elif board[0][2] == 0:
        board[0][2] = 2
    elif board[1][0] == 0:
        board[1][0] = 2
    elif board[1][1] == 0:
        board[1][1] = 2
    elif board[2][1] == 0:
        board[2][1] = 2
    elif board[2][2] == 0:
        board[2][2] = 2
    return(board)

# Move Six
def move_six(board):
    if board[0][1] == 0:
        board[0][1] = 2
    elif board[0][2] == 0:
        board[0][2] = 2
    elif board[1][0] == 0:
        board[1][0] = 2
    elif board[1][1] == 0:
        board[1][1] = 2
    elif board[2][1] == 0:
        board[2][1] = 2
    elif board[2][2] == 0:
        board[2][2] = 2
    return(board)

# Move Seven
def move_seven(board):
    if board[0][0] == 0:
        board[0][0] = 2
    elif board[1][0] == 0:
        board[1][0] = 2
    elif board[1][1] == 0:
        board[1][1] = 2
    elif board[0][2] == 0:
        board[0][2] = 2
    elif board[2][1] == 0:
        board[2][1] = 2
    elif board[2][2] == 0:
        board[2][2] = 2
    return(board)

# Move Eight
def move_eight(board):
    if board[0][1] == 0:
        board[0][1] = 2
    elif board[1][0] == 0:
        board[1][0] = 2
    elif board[1][1] == 0:
        board[1][1] = 2
    elif board[1][2] == 0:
        board[1][2] = 2
    elif board[2][0] == 0:
        board[2][0] = 2
    elif board[2][2] == 0:
        board[2][2] = 2
    return(board)

# Move Nine
def move_nine(board):
    if board[0][0] == 0:
        board[0][0] = 2
    elif board[0][2] == 0:
        board[0][2] = 2
    elif board[1][1] == 0:
        board[1][1] = 2
    elif board[1][2] == 0:
        board[1][2] = 2
    elif board[2][0] == 0:
        board[2][0] = 2
    elif board[2][1] == 0:
        board[2][1] = 2
    return(board)
    
            
#Computer's Move (The Function that you can modify according to your wish)
def computer_move(board, player_pos):
    if player_pos == 1:
        board = move_one(board)
    elif player_pos == 2:
        board = move_two(board)
    elif player_pos == 3:
        board = move_three(board)
    elif player_pos == 4:
        board = move_four(board)
    elif player_pos == 5:
        board = move_five(board)
    elif player_pos == 6:
        board = move_six(board)
    elif player_pos == 7:
        board = move_seven(board)
    elif player_pos == 8:
        board = move_eight(board)
    elif player_pos == 9:
        board = move_nine(board)
    return(board)
     
     
# Horizontal win Check
def row_win(board, player):
    for x in range(len(board)):
        win = True
        
        if player == 1:
            player = 1
        else:
            player = 2
        
        for y in range(len(board)):
            if board[x][y] != player:
                win = False
                continue
        if win == True:
            return(win)
    return(win)

# Vertical win Check
def col_win(board, player):
    for x in range(len(board)):
        win = True
        
        if player == 1:
            player = 1
        else:
            player = 2
        
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
        if win == True:
            return(win)
    return(win)

# Diagonal win check
def diag_win(board, player):
    win = True
    
    if player == 1:
        player = 1
    else:
        player = 2
    
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return(win)
        
# Evaluation
def evaluate(board):
    winner = 0
    
    for player in [1, 2]:
        if (row_win(board, player) or
            col_win(board, player) or
            diag_win(board, player)):
            
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
                     
                    
    
# Main game function
def game():
    board, winner, counter = create_board(), 0, 1
    print("The Game is On...")
    print("Position is from 1 to 9")
    print("You are 1 and Computer is 2")
    print(board)
    sleep(2)
    
    while winner == 0:
        player_pos = int(input("Enter Position: "))
        board = player_move(board, player_pos)
        print("Board after " + str(counter) + " move")
        print(board)
        counter += 1
        winner = evaluate(board)
        if(winner == 1):
            winner = 'You'
            break
        elif(winner == -1):
            winner = 'No Winner'
            break
        else:
            winner = 0
        print("Computer is thinking...")
        sleep(2)
        board = computer_move(board, player_pos)
        print("Board after " + str(counter) + " move")
        print(board)
        counter += 1
        winner = evaluate(board)
        if(winner == 2):
            winner = 'Computer'
            break
        elif(winner == -1):
            winner = 'No Winner'
            break
        else:
            winner = 0
    return(winner)
    
        
# Driver Code
print("Winner is : " + str(game()))