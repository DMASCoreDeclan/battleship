import os
from time import sleep

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
After each guess, the board with results of your previous guesses will be displayed,\n\
the number of bombs you have remaining\n \
At the end of the game you will be asked if you want to play again or return to the main menu.\n\
X - Hit\n\
* - Miss\n\
| | Available as a target\n")
    sleep(7)
    os.system('clear')

def get_user_preferences():
    name = input("What is your name: \n")
    print(f"Thank you {name}")
    grid_size = input("What size grid would you like to play: \n")
    return(name, grid_size)

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
    os.system('clear')
    welcome_message()
    name, grid_size = get_user_preferences()
    print(name, grid_size)
    draw_board()
    request_guess()
    validate_guess()
    place_guess()
    check_winner()
    check_lives()


main()