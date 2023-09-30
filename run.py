import os  # for clear()
from time import sleep  # delay time before # clear() is used
from random import randint  # for generating random numbers

name = ""
game_on = True
grid_size = 0


def clear():
    """
    clears the sreen so that it doesn't become too crowded with previous
    interactions
    """
    os.system("clear")


def welcome():
    """
    This message will appear whenever the game starts or restarts with a new
    player, it explains how the game works.
    * denotes a HIT
    X denotes a MISS from a previous guess
    | | decontes a potential space for a guess
    The Welcome and Instructions will disappear after 7 seconds
    """
    clear()
    print("Welcome to Battleships\n")
    print(
        "This game is designed to allow you to select the grid size you want\
            \nto play in, the number of ships you want the computer to place\
            \nin the grid and determine the number of bombs you want to be\
            \nable to use.  The grid size is a square and can be between 4x4\
            \n and 10x10 in size.  After each guess, the board with results\
            \nof your previous guesses will be displayed and the number of\
            \nbombs you have remaining. At the end of the game you will be\
            \n asked if you want to play again or return to the main menu.\
            \n* - Hit\
            \nX - Miss\
            \n| | Available as a target\
            \n"
    )
    sleep(1)
    # clear()


def get_player_name():
    """
    Asks for user input for NAME.
    """
    global name
    name = input("What is your name: \n")
    print(f"Thank you {name}")
    sleep(1)
    # clear()


def new_player():
    welcome()
    get_player_name()


def get_grid_size(name):
    """
    Validates user input so that the choices they make for the grid_size are
    within the boundaries of the program.  Asks the user to enter new inputs
    until they are acceptable.
    Returns a validated GRID_SIZE.
    """
    while True:
        try:
            clear()
            grid_size = int(
                input(
                    f"{name}, what size grid do you want to use?\
            \nPick a number between 4 and 10:\n"
                )
            )
            if grid_size >= 4 and grid_size <= 10:
                clear()
                print(f"Good choice {name}")
                return grid_size
        except ValueError:
            print("Thats not a valid number")


def get_ships_value(name):
    """
    Validates user input so that the choices they make for the number of
    ships are within the boundaries of the program.  Asks the user to enter
    new inputs until they are acceptable.
    Returns a valid number of SHIPS
    """
    while True:
        try:
            ships = int(
                input(
                    f"{name}, how many ships do you want to pursue?  \
                              \nPick a number between 1 and 5:\n"
                )
            )
            if ships >= 1 and ships <= 5:
                return ships
        except ValueError:
            print("Thats not a valid number")


def get_bomb_value(name, grid_size):
    """
    Validates user input so that the choices they make for the nu,ber of bombs
    are within the boundaries of the program.  Asks the user to enter new
    inputs until they are acceptable.  Returns a calculated number of BOMBS.
    The calculation multiplies the GRID_SIZE by itself giving the total
    possible number of locations where the SHIPS might be.  Depending on how
    adventurous the user feels, they can decide whether they want the game to
    be EASY, DIFFICULT or IMPOSSIBLE.
    """
    while True:

        try:
            clear()
            bombs = input(
                f"{name}, what level of difficulty are you looking for?\
                \nEasy gives you {(grid_size * grid_size) - 1} of the \
                {(grid_size * grid_size)} bombs required\
                \nDifficult gives you 75% or \
                {round((grid_size * grid_size) * .75)} \
                of the bombs you require\
                \nImpossible gives you 50% or \
                {round((grid_size * grid_size) * .5)}\
                 of the bombs you require\
                \nPress E for Easy\
                \nPress D for Difficult\
                \nPress I for Impossible\
                \nThe default is: Impossible"
            ).upper()
            if bombs in "EDI":
                if bombs == "E":
                    bombs = (grid_size * grid_size) - 1
                elif bombs == "D":
                    bombs = (grid_size * grid_size) * 0.75
                else:
                    bombs = (grid_size * grid_size) * 0.5
                print(f"Good luck {name}")
                sleep(3)
                clear()
                return int(bombs)
        except ValueError:
            print("Thats not a valid letter")


def prepare_computer_board(grid_size):
    computer_board = [
        [" "] * grid_size for x in range(grid_size)
    ]  # records the computer location of ships for testing purposes
    return computer_board


def prepare_guess_board(grid_size):
    previous_guess_board = [[" "] * grid_size for x in range(grid_size)]
    return previous_guess_board


def new_game():
    clear()
    global grid_size, ships, bombs, computer_board, previous_guess_board
    grid_size = get_grid_size(name)
    ships = get_ships_value(name)
    bombs = get_bomb_value(name, grid_size)
    computer_board = prepare_computer_board(grid_size)
    previous_guess_board = prepare_guess_board(grid_size)
    print(
        f"Thank you for your patience {name}\
          \nYou have chosen to play with a grid: {grid_size} x {grid_size} in size with {ships} ships and {bombs} bombs.\
          \nPreparing your game . . ."
    )
    sleep(5)
    return grid_size, ships, bombs, computer_board, previous_guess_board


def draw_board(board, grid_size):
    """
    This function requires 2 inputs: a BOARD type and the previously supplied
    GRID_SIZE.  It then draws a board with letters as headings and numbers as#
    row values.  The user will use the Letter and Number input to determine
    where they would like to place their next guess.
    Returns HEADING1 which is the list of valid letters that the user must
    choose fom later.
    """
    clear()
    heading1 = "  A B C D E F G H I J "  # Heading for Grid
    heading2 = " ---------------------"  # Heading decorator for Grid
    heading_value = (
        grid_size * 2
    ) + 2  # There are 2 leading spaces and each row requires 2 spaces
    print(heading1[:heading_value])
    print(heading2[:heading_value])
    grid_row = 0  # begins the row numbering at 0
    for row in board:
        print(
            "%d|%s|" % (grid_row, "|".join(row))
        )  # %s and %d are placeholders for a string and a number
        # respectively. %s returns the string and %d returns a
        # number.  The values are passed using % operator
        grid_row += 1
    return heading1[:heading_value]


def place_ships(board, grid_size, ships):
    """
    identifies a location for the computer to locate their SHIPS based on the
    user supplied GRID_SIZE and number of SHIPS.  The for an while keep going
    until the correct number of SHIPS have been placed in the correct
    location of the user defined GRID_SIZE.
    Return a populated board with *s according to the input in
    GET_USER_PREEFERENCES
    """
    for ship in range(ships):
        ship_row = randint(0, (grid_size - 1))
        ship_letter = randint(0, (grid_size - 1))

        while board[ship_row][ship_letter] == "*":
            ship_letter = randint(0, (grid_size - 1))
            ship_row = randint(0, (grid_size - 1))
        board[ship_row][ship_letter] = "*"


def prepare_boards():
    clear()
    draw_board(previous_guess_board, grid_size)
    draw_board(computer_board, grid_size)
    place_ships(computer_board, grid_size, ships)
    clear()
    print(f"I've placed my ships {name}")
    print("Get ready to play . . .")
    sleep(3)


def get_letter(heading_value):
    """
    Validates user input so that the choice they make for the letter of
    the column exists in the grid.  The letter is converted to a number
    from the LETTER_MAP dictionary.
    Returns a letter input as a 0 based index number.
    """
    letter_map = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
    }  # used to convert the heading letter into a number
    while True:
        try:
            ship_column = input(
                f"{name}, please pick a letter from {heading_value[0]} - {heading_value[-1]}\n"
            ).upper()
            if ship_column in heading_value:
                return letter_map[ship_column]
            else:
                print("Thats not a valid letter")
        except KeyError:
            print("Thats not a valid input")


def get_number(grid_size):
    """
    Validates user input so that the choice they make for the number of the
    row exists in the grid.
    Returns a 0 based index number.
    """
    while True:
        try:
            ship_row = int(
                input(f"{name}, please pick a number from 0 - {grid_size -1}\n")
            )
            if ship_row <= (grid_size - 1):
                return ship_row
            else:
                print("Thats not a valid number")
        except (KeyError, ValueError) as error:
            print("Thats not a valid number")


def request_guess(heading_value, grid_size):
    """
    Requests user input for a letter and a number to identify where the user
    wants to place their bomb.  The input is validated against the limitations
    of the parameters that they chose in get_user_preferences.  If its not a
    valid input, they are requested for the information until it is valid.
    Returns a valid set of 0 based numbers within the GRID_SIZE
    """
    ship_column = get_letter(heading_value)
    ship_row = get_number(grid_size)
    return ship_row, ship_column


def get_heading_value():
    heading_value = draw_board(previous_guess_board, grid_size)
    heading_value = heading_value.replace(" ", "")
    return heading_value


def count_hit_ships():
    hits = 0
    for row in previous_guess_board:
        for column in row:
            if column == "*":
                hits += 1
    return hits


def validate_guess(ship_row, ship_column, bombs, ships):
    clear()
    if (
        previous_guess_board[ship_row][ship_column] == "X"
        or previous_guess_board[ship_row][ship_column] == "*"
    ):
        print(f"Come on {name}, you already guessed that")
    elif computer_board[ship_row][ship_column] == "*":
        print(f"Excellent {name}, you have hit a battleship")
        previous_guess_board[ship_row][ship_column] = "*"
        bombs -= 1
    else:
        print("You missed")
        previous_guess_board[ship_row][ship_column] = "X"
        bombs -= 1
    print(f"You have {bombs} bombs left")
    print(f"You have {ships - count_hit_ships()} ships left to hit")
    if bombs < (ships - count_hit_ships()):
        print(f"\nYou cannot win! {name}")
    sleep(3)
    return bombs


def main(bombs, ships, grid_size):
    while bombs > 0 and count_hit_ships() != ships:
        print(f"declan has {bombs} bombs")
        ship_row, ship_column = request_guess(get_heading_value(), grid_size)
        bombs = validate_guess(ship_row, ship_column, bombs, ships)
        print(
            f"You have hit {count_hit_ships()} ships and have \
                {ships - count_hit_ships()} ships left to hit."
        )
        if bombs == 0:
            print("You have no bombs left!")
        elif bombs == 1:
            print(f"You still have {bombs} bomb")
        else:
            print(f"You still have {bombs} bombs")


while game_on:
    if name == "":
        welcome()
        get_player_name()
    clear()
    play = input(
        f"Would you like to play Battleships {name}?\n\
                 \nPress P to Play\n\
                 \nPress Q to Quit the game\n\
                 \nPress any other key to change the players name\n\
                 \n"
    ).upper()
    if play == "P":
        grid_size, ships, bombs, computer_board, previous_guess_board = new_game()
        place_ships(computer_board, grid_size, ships)
        main(bombs, ships, grid_size)
    elif play == "Q":
        game_on = False
    else:
        name = ""
