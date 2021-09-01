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


# 06 If invalid input othr than Y/N prompts again
def invalid_input():
    start()


# 06 Play again when game ends
def play_again():
    print("\n")
    # Ask user for another game
    start = input("Would you like to play another game? Y/N: ").upper()
    # If yes resest the game
    if start.upper() == "Y":
        # Reset board
        global board
        board = ["*", "*", "*", "*", "*", "*", "*", "*", "*"]
        # Reset ongoing_game
        global ongoing_game
        ongoing_game = True
        # Reset current player back to X
        global current_player
        current_player = "X"
        # Reset winner to none
        global winner
        winner = None
        # Run Game
        play_game()
        # Exit if N was typed
    elif start.upper() == "N":
        exit
    else:
        # Error if invalid character was input
        print("Invalid character, Please run again")
        invalid_input()


# 05 Swap the current player from X to O, or O to X
def swap_player():
    # Global variable we need
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"


# 4.5 Check if there is a tie
def check_for_tie():
    # Set global variable
    global ongoing_game
    # If board is full stop game
    if "*" not in board:
        ongoing_game = False
        # And print game is a tie
        print("Game is a Tie! \n")
        play_again()
        return True
    # Else there is no tie
    else:
        return False


# 4.4 Check the diagonals for a win
def check_diagonals():
    # Set global variable
    global ongoing_game
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "*"
    diagonal_2 = board[2] == board[4] == board[6] != "*"
    # If any diagonal row has a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        ongoing_game = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# 4.3 Check the columns for a win
def check_columns():
    # Set global variable
    global ongoing_game
    # Check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "*"
    column_2 = board[1] == board[4] == board[7] != "*"
    column_3 = board[2] == board[5] == board[8] != "*"
    # If any columns have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        ongoing_game = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# 4.2 Check the rows for a win
def check_rows():
    # Set global variable
    global ongoing_game
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "*"
    row_2 = board[3] == board[4] == board[5] != "*"
    row_3 = board[6] == board[7] == board[8] != "*"
    # If any rows have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        ongoing_game = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    # Or return None if there was no winner
    else:
        return None


# 4.1 Check for winner
def check_for_winner():
    # Set global variable
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
    # Check for winner
    check_for_winner()
    # Check for tie
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
    print("-------------------------------------")
    print("|  " + board[0] + " | " + board[1] +
          " | " + board[2] + "             1 | 2 | 3  |")
    print("|  " + board[3] + " | " + board[4] +
          " | " + board[5] + "  TicTacToe  4 | 5 | 6  |")
    print("|  " + board[6] + " | " + board[7] +
          " | " + board[8] + "             7 | 8 | 9  |")
    print("-------------------------------------")
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
        global board
        if winner == "X" or winner == "O":
            print("<-------- Congratulations " +
                  winner + ", you win. -------->")
            play_again()


# Prompt user to start game
def start():
    display_board()
    print("\n")
    start = input("Would you like to play a game? Y/N: ").upper()
    # If yes play game
    if start.upper() == "Y":
        play_game()
    # if no exit
    elif start.upper() == "N":
        exit
    # if invalid input print
    else:
        print("Invalid character, Please run again")
        invalid_input()


# ------- Execute -------

# Start a game of tic tac toe
print("\n")
print("Welcome to Clayton's TicTacToe Multiplayer Game")
start()
