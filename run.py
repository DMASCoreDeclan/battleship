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
    sleep(3)
    clear()

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

def new_player():
    welcome()
    get_player_name()
    
def new_game():
    clear()
    grid_size = get_grid_size(name)
    ships = get_ships_value(name)
    print("newgame", grid_size, ships)

def main():
    while name == "":
        welcome()
        get_player_name()
    new_game()



    

main()


