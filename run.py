import os # for clear()
from time import sleep # delay time before clear() is used

def clear():
    """
    clears the sreen so that it doesn't become too crowded with previous interactions
    """
    os.system('clear')
    
def welcome():
    """
    This message will appear whenever the game starts or restarts with a new player,
    it explains how the game works.
    * denotes a HIT
    X denotes a MISS from a previous guess
    | | decontes a potential space for a guess
    The Welcome and Instructions will disappear after 7 seconds
    """
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
    sleep(7)
    clear()

def get_player_name():
    """
    Asks for user input for NAME.      
    """
    global name
    name = input("What is your name: \n")
    print(f"Thank you {name}")
    sleep(3)
    clear()


def new_game():
    welcome()
    get_player_name()
    


def main():
    new_game()

main()


