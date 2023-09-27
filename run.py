import os
from time import sleep


grid_size = 0
ships = 1
name = ""
bombs = grid_size * .5
COLUMN_HEADINGS = 'ABCDEFGHIJ'
COMPUTER_BOARD = [[' '] * grid_size for x in range(grid_size)]
PREVIOUS_GUESS_BOARD = [[' '] * grid_size for x in range(grid_size)]

letter_conversion = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 
}
def clear():
    os.system('clear')

def welcome_message():
    """
    This message will appear whenever the game starts or restarts, it explains how
    the game works.
    X denotes a HIT
    * denotes a MISS from a previous guess
    | | decontes a potential space for a guess
    The Welcome and Instructions will disappear after 7 seconds
    """
    print("Welcome to Battleships\n")
    print("This game is designed to allow you to select the grid size you want to play in,\n\
the number of ships you want the computer to place in the grid and determine\n\
the number of bombs you want to be able to use.\n\
The grid size is a square and can be between 4x4 and 10x10 in size.\n\
After each guess, the board with results of your previous guesses will be displayed and\n\
the number of bombs you have remaining\n \
At the end of the game you will be asked if you want to play again or return to the main menu.\n\
X - Hit\n\
* - Miss\n\
| | Available as a target\n")
    sleep(7)
    clear()

def get_grid_size(name):
    while True: 
        try:  
            grid_size = int(input(f"{name}, what size grid do you want to use?  \n\
Pick a number between 4 and 10:\n"))          
            if grid_size >= 4 and grid_size <= 10:
                print(f"Good choice {name}")
                return grid_size
        except ValueError:
                print("Thats not a valid number")


def check_ships_value(name):
    while True: 
        try:  
            ships = int(input(f"{name}, how many ships do you want to pursue?  \n\
Pick a number between 1 and 5:\n"))        
            if ships >= 1 and ships <= 5:
                return ships
        except ValueError:
                print("Thats not a valid number")
    

def check_bomb_value(name):
    while True:    
        try:  
            bombs = int(input(f"{name}, whats the maximum number of bombs you want to use  \n\
Pick a percentage between 5 and 50:\n"))         
            if bombs >= 5 and bombs <= 50:
                print(f"Good choice {name}")
                return bombs / 100 # turns int into a percentage
        except ValueError:
                print("Thats not a valid number")

def get_user_preferences():
    name = input("What is your name: \n")
    print(f"Thank you {name}")
    grid_size = get_grid_size(name)
    print(grid_size)
    ships = check_ships_value(name)
    print(ships)
    bombs = check_bomb_value(name)
    bombs = (bombs * grid_size * grid_size)
    print(bombs)
    print(f"{name}, you have chosen to play on a {grid_size} x {grid_size} grid with {ships} ships\n\
with {bombs} bombs!  Good Luck!")
    return(name, grid_size, ships, bombs)

def draw_board():
    pass

def request_guess():
    pass

def validate_guess():
    pass

def place_guess():
    pass

def check_winner():
    pass

def check_lives():
    pass


    

def build_grid(grid_size):
    pass



def main():
    clear()
    welcome_message()
    name, grid_size, ships, bombs = get_user_preferences()
    print(name, grid_size, ships, bombs)
    draw_board()
    request_guess()
    validate_guess()
    place_guess()
    check_winner()
    check_lives()


main()