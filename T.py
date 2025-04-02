import math

# Function to display the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print('|'.join(row))
    print('\n')
    
# Function to check if there are any moves left 
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False

# Function to evaluate the board
def evaluate(board):
    # Check rows and columns for win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return 10 if row[0] == 'X' else -10
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] !=" ":
            return 10 if board[0][col] == 'X' else -10
        
    # Check diagonals for win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] !=" ":
        return 10 if board[0][0] == "X" else -10
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] !=" ":
        return 10 if board[0][2] == 'X' else -10
    
    return 0

# Minimax algorithm implementation
def minimax(board, depth, is_max):
    score = evaluate(board)
    
    #If Maximizer (AI) wins
    if score == 10:
        return score - depth
    
    #If Minimizer (human) wins
    if score == -10:
        return score + depth
    
    #If no more moves left (draw)
    if not is_moves_left(board):
        return 0
    
    #Maximizer's move 
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j]=" "
        return best
    
    # Minimizer's move
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] ==' ':
                    board[i][j] = '0'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best
    
# Function to find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j]= ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i,j)
                    
    return best_move

# Main function to play the game
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        # Human's move
        print("Your turn (0):")
        while True:
            try:
                row, col = map(int, input("Enter row and column (0, 1, 2): ").split())
                if board[row][col] == " ":
                    board[row][col] = '0'
                    break
                else:
                    print('Cell already occupied, try again.')
            except:
                print('Invalid input. Enter two numbers separated by a space (e.g., 0 1).')
        print_board(board)
        
        #Check if human won
        if evaluate(board) == -10:
            print('You win!')
            break
            
        #Check for draw
        if not is_moves_left(board):
            print("It's a Dwar!")
            break
            
        #AI's move
        print("AI's turn (X):")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'
        print_board(board)
        
        #Check if AI won
        if evaluate(board) == 10:
            print('AI wins!')
            break
            
        #Check for Draw
        if not is_moves_left(board):
            print("It's a Draw!")
            break
            
# Run the game
play_tic_tac_toe()
