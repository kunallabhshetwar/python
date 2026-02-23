import random

# Board Display
def display_board(board):
    print("\n")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("\n")

# Player Input
def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player 1, choose X or O: ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Place Marker

def place_marker(board, marker, position):
    board[position] = marker

# Win Check

def win_check(board, mark):
    return (
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        (board[7] == board[4] == board[1] == mark) or
        (board[8] == board[5] == board[2] == mark) or
        (board[9] == board[6] == board[3] == mark) or
        (board[7] == board[5] == board[3] == mark) or
        (board[9] == board[5] == board[1] == mark)
    )

# Choose First Player

def choose_first():
    return random.choice(['Player 1', 'Player 2'])

# Space Check

def space_check(board, position):
    return board[position] == ' '

# Full Board Check

def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

# Player Choice

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("Choose your position (1-9): "))
    return position

# Replay

def replay():
    return input("Play again? (y/n): ").lower().startswith('y')

# Game Loop

print("Welcome to Tic Tac Toe")

while True:
    # Board setup
    theBoard = [' '] * 10

    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    play_game = input("Ready to play? (y/n): ").lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1 Turn
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("🎉 Player 1 wins! Congratulations!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("🤝 It's a draw!")
                    break
                else:
                    turn = 'Player 2'

        # Player 2 Turn
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("🎉 Player 2 wins! Congratulations!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("🤝 It's a draw!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        print("Thanks for playing Tic Tac Toe! 👋")
        break