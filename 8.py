from collections import deque

# Function to print the puzzle board
def print_board(board):
    for row in board:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print('\n')

# Function to check if the puzzle is solvable
def is_solvable(puzzle):
    flat_puzzle = [num for row in puzzle for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

# Function to find the position of the empty tile (0)
def find_empty_tile(puzzle):
    for i, row in enumerate(puzzle):
        for j, value in enumerate(row):
            if value == 0:
                return i, j

# Function to generate possible moves from the current puzzle state
def generate_moves(puzzle):
    row, col = find_empty_tile(puzzle)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            # Copy the puzzle and make the move
            new_puzzle = [list(r) for r in puzzle]
            new_puzzle[row][col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[row][col]
            moves.append(new_puzzle)
    return moves

# BFS algorithm to solve the 8-puzzle problem
def solve_puzzle(start, goal):
    if not is_solvable(start):
        return "The puzzle is not solvable."

    queue = deque([(start, [])])  # (current_state, path_to_current_state)
    visited = set()
    visited.add(tuple(tuple(row) for row in start))

    while queue:
        current, path = queue.popleft()

        # Check if the current state is the goal state
        if current == goal:
            return path + [current]

        # Generate and explore all valid moves
        for move in generate_moves(current):
            move_tuple = tuple(tuple(row) for row in move)
            if move_tuple not in visited:
                visited.add(move_tuple)
                queue.append((move, path + [current]))

    return "No solution found."

# Function for the player to make a move manually
def player_move(board):
    while True:
        try:
            print("Enter the tile number you want to move (e.g., 1, 2, 3...):")
            move = int(input())
            empty_row, empty_col = find_empty_tile(board)

            # Find the tile position
            tile_row, tile_col = -1, -1
            for i in range(3):
                for j in range(3):
                    if board[i][j] == move:
                        tile_row, tile_col = i, j
                        break

            # Check if the move is valid
            if (abs(tile_row - empty_row) == 1 and tile_col == empty_col) or \
               (abs(tile_col - empty_col) == 1 and tile_row == empty_row):
                board[empty_row][empty_col], board[tile_row][tile_col] = board[tile_row][tile_col], board[empty_row][empty_col]
                return board
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number corresponding to a tile.")

# Main function to play the 8-puzzle game
def play_8_puzzle():
    start_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    print("Welcome to the 8-Puzzle Game!")
    print("Start State:")
    print_board(start_state)
    print("Goal State:")
    print_board(goal_state)

    # Check if the puzzle is solvable
    if not is_solvable(start_state):
        print("The start configuration is not solvable.")
        return

    while True:
        # Player's move
        print("Your move:")
        start_state = player_move(start_state)
        print_board(start_state)

        # Check if the player reached the goal
        if start_state == goal_state:
            print("Congratulations! You solved the puzzle!")
            break

        # AI's move
        print("AI is solving the puzzle...")
        solution = solve_puzzle(start_state, goal_state)
        if isinstance(solution, str):
            print(solution)
            break
        else:
            print("AI's next move:")
            start_state = solution[1]  # AI performs the next step
            print_board(start_state)

            # Check if AI reached the goal
            if start_state == goal_state:
                print("AI solved the puzzle!")
                break

# Run the game
play_8_puzzle()
