# ------- Global Variables -------

# Our New Game Board
board = ["*", "*", "*",
         "*", "*", "*",
         "*", "*", "*"]

# Game in progress / finsihed
ongoing_game = True

# Game winner
winner = None

# Current Player (X starts first)
current_player = "X"

# ------- Functions -------


# 4.5 Check for winner
def check_for_winner():
    # Set global variables
    global winner
    # Check rows, columns and diagonals for a winning line
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# 04 Check for game end
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# 03 Handle a turn
def handle_turn(player):
    # Get position from player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    # Check input is valid
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
    # Get correct index in our board list
    position = int(position) - 1
    # Check position is available
    if board[position] == "*":
        valid = True
    else:
        print("Position taken, please try again")
    # Mark the board
    board[position] = player
    # Display game board
    display_board()


# 02 Display the game board to the screen
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# 01 Play a game of tic tac toe
def play_game():
    # Show the initial game board
    display_board()
    # Loop until the game stops (winner or tie)
    while ongoing_game:
        # Handle a turn
        handle_turn(current_player)
        # Check if the game is over
        check_if_game_over()
        # Swap to the other player
        swap_player()
        # Since the game is over, print the winner or tie
        if winner == "X" or winner == "O":
            print("Congratulations " + winner + ", you win.")
        elif winner == None:
            print("The game is a tie.")


# ------- Execute -------

# Start a game of tic tac toe
play_game()