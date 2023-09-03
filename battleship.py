import random

# Initialize the board
board_size = 5
board = [["O" for _ in range(board_size)] for _ in range(board_size)]

# Create the computer's ships
computer_ships = [(random.randint(0, board_size - 1), random.randint(0, board_size - 1)) for _ in range(3)]

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

# Function to check if a coordinate is valid
def is_valid_coordinate(x, y):
    return 0 <= x < board_size and 0 <= y < board_size

# Function to check if a ship is hit
def is_ship_hit(x, y, ships):
    return (x, y) in ships

# Game loop
turns = 8  # Set the number of turns
for turn in range(turns):
    print(f"Turn {turn + 1}/{turns}")
    
    # Player's turn
    while True:
        try:
            x, y = map(int, input("Enter target coordinates (x y): ").split())
            if is_valid_coordinate(x, y):
                break
            else:
                print("Invalid coordinates. Try again.")
        except ValueError:
            print("Invalid input. Enter coordinates as two numbers separated by space.")

    if is_ship_hit(x, y, computer_ships):
        print("Congratulations, You have hit a computer's ship!")
        board[x][y] = "X"
        computer_ships.remove((x, y))
    else:
        print("You missed!")

    # Check if the player has won
    if not computer_ships:
        print("Congratulations! You've sunk all of the computer's ships!")
        break

    print_board(board)

# End of the game
print("Game over. The computer's ships were located at:")
for x, y in computer_ships:
    print(f"({x}, {y})")
