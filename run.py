import os
from time import sleep

def welcome_message():
    pass

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
