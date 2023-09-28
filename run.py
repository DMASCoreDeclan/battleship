import os # for clear()
from time import sleep # delay time before clear() is used
name = ""
game_on = True

def clear():
    """
    clears the sreen so that it doesn't become too crowded with previous interactions
    """
    os.system('cls')
        
def welcome():
    """
    This message will appear whenever the game starts or restarts with a new player,
    it explains how the game works.
    * denotes a HIT
    X denotes a MISS from a previous guess
    | | decontes a potential space for a guess
    The Welcome and Instructions will disappear after 7 seconds
    """
    clear()
    print("Welcome to Battleships\n")
    print("This game is designed to allow you to select the grid size you want to play in,\
          \nthe number of ships you want the computer to place in the grid and determine\
          \nthe number of bombs you want to be able to use.\
          \nThe grid size is a square and can be between 4x4 and 10x10 in size.\
          \nAfter each guess, the board with results of your previous guesses will be displayed and\
          \nthe number of bombs you have remaining.\
          \nAt the end of the game you will be asked if you want to play again or return to the main menu.\
          \n* - Hit\
          \nX - Miss\
          \n| | Available as a target\
          \n")
    sleep(1)
    clear()

def get_player_name():
    """
    Asks for user input for NAME.      
    """
    global name
    name = input("What is your name: \n")
    print(f"Thank you {name}")
    sleep(1)
    clear()

def new_player():
    welcome()
    get_player_name()

def get_grid_size(name):
    """
    Validates user input so that the choices they make for the grid_size are within the boundaries 
    of the program.  Asks the user to enter new inputs until they are acceptable. 
    Returns a validated GRID_SIZE. 
    """
    while True: 
        try:
            clear()  
            grid_size = int(input(f"{name}, what size grid do you want to use?\
            \nPick a number between 4 and 10:\n"))          
            if grid_size >= 4 and grid_size <= 10:
                print(f"Good choice {name}")
                
                return grid_size
        except ValueError:
                print("Thats not a valid number")

def get_ships_value(name):
    """
    Validates user input so that the choices they make for the number of ships are within
    the boundaries of the program.  Asks the user to enter new inputs until they are acceptable.  
    Returns a valid number of SHIPS
    """
    while True: 
        try:  
            clear()
            ships = int(input(f"{name}, how many ships do you want to pursue?  \n\
Pick a number between 1 and 5:\n"))        
            if ships >= 1 and ships <= 5:
                return ships
        except ValueError:
                print("Thats not a valid number")

def get_bomb_value(name, grid_size):
    """
    Validates user input so that the choices they make for the nu,ber of bombs are within the 
    boundaries of the program.  Asks the user to enter new inputs until they are acceptable.  
    Returns a calculated number of BOMBS.  The calculation multiplies the GRID_SIZE by itself
    giving the total possible number of locations where the SHIPS might be.  Depending on how 
    adventurous the user feels, they can decide what percentage of possible locations they can 
    shoot at, before the game begins.  The minimum value is 5% and the maximum value is 50%.
    """
    while True:    
        try:  
            clear()
            bombs = int(input(f"{name}, whats the maximum number of bombs you want to use  \
                              \nPick a percentage between 1 and 99:\n"))         
            if bombs >= 1 and bombs <= 99:
                print(f"Good choice {name}")
                return bombs / 100 # turns int into a percentage
        except ValueError:
                print("Thats not a valid number")

def prepare_computer_board(grid_size):
    computer_board = [[' '] * grid_size for x in range(grid_size)] # records the computer location of ships for testing purposes
    return computer_board

def prepare_guess_board(grid_size):
    previous_guess_board = [[' '] * grid_size for x in range(grid_size)]
    return previous_guess_board

def new_game():
    clear()
    global grid_size, ships, bombs, computer_board, previous_guess_board
    grid_size = get_grid_size(name)
    ships = get_ships_value(name)
    bombs = get_bomb_value(name, grid_size)
    bombs = grid_size * grid_size * bombs
    computer_board = prepare_computer_board(grid_size)
    previous_guess_board = prepare_guess_board(grid_size)
    print(f"Thank you for your patience {name}\
          \nYou have chosen to play with a grid: {grid_size} x {grid_size} in size\
          \nwith {ships} ships and {bombs} bombs.\
          \nPreparing your game . . ")
    sleep(3)
    clear()    

def draw_board(board, grid_size):
    """
    This function requires 2 inputs: a BOARD type and the previously supplied GRID_SIZE.
    It then draws a board with letters as headings and numbers as row values.  The user
    will use the Letter and Number input to determine where they would like to place their 
    next guess.  
    Returns HEADING1 which is the list of valid letters that the user must choose fom later.
    """
    clear()
    print(grid_size)
    heading1 = "  A B C D E F G H I J " # Heading for Grid
    heading2 = " ---------------------" # Heading decorator for Grid
    heading_value = (grid_size * 2) + 2 # There are 2 leading spaces and each row requires 2 spaces
    print(heading1[:heading_value])
    print(heading2[:heading_value])
    grid_row = 0 #  begins the row numbering at 0
    for row in board:
        print("%d|%s|" % (grid_row, "|".join(row))) # %s and %d are placeholders for a string and a number respectively. %s returns the string and %d returns a number.  The values are passed using % operator
        grid_row +=1
    return heading1[:heading_value]

def prepare_boards():
     draw_board(computer_board, grid_size)
     draw_board(previous_guess_board, grid_size)

def main():
    while name == "":
        welcome()
        get_player_name()
    new_game()
    prepare_boards()


    

main()


