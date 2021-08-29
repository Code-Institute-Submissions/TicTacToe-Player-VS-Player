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