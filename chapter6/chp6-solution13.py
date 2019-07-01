'''
Victor Montoya
Chapter 6 Solution 13
Slot Machines
28 June 2019
'''

# Constants for score multiplying
TWO_SCORE = 2
THREE_SCORE = 3

# Sentinel constant
END = -99

# Importing random module
import random

# global variables that hold all symbols to be randomized
options = ["Cherries", "Oranges", "Plums", "Bells", "Melons", "Bars"]

# Global variable user money holds initial balance of 100, user_input will hold users amount entered
user_money = 100
user_input = None

# Global variables will hold the random symbols
symbol_one = None
symbol_two = None
symbol_three = None

def main():
    print("\nWelcome to the XYZ Slot Machine")
    randomize_choices()
    request_money()

def request_money():
    # Declares user money and user input as global variables
    global user_money
    global user_input

    # Displays balance and user enters amount into machine, then assigned to user input global variable
    print("You have $", user_money)
    user_input = int(input("Enter a wager amount(-99 to QUIT): $"))

    # If users input is more than their balance, it makes user try a lesser amount
    if user_input > user_money:
        user_input = int(input("You don't have that amount of money, enter a lesser amount(-99 to QUIT): $"))
    # If user input equals -99 it will exit program
    elif user_input == END:
        exit()
    check_score()

def randomize_choices():
    # Declares symbol variables as global variables
    global symbol_one
    global symbol_two
    global symbol_three

    # Assigns random symbols to global variables
    symbol_one = random.choice(options)
    symbol_two = random.choice(options)
    symbol_three = random.choice(options)
    
def check_score():
    # Declares user money as global variablw
    global user_money

    # prints random symbos
    print(symbol_one, " ", symbol_two, " ", symbol_three)

    # If all 3 symbols are the same, user wins triple the entered amount, prints prize adnd adds to balance
    if symbol_one == symbol_two and symbol_two == symbol_three:
        win_amount = user_input * THREE_SCORE
        user_money += win_amount
        print("YOU WIN! $", win_amount, "\n")
    # If only 2 symbols are the same, user wins double the entered amount, prints prize and adds to balance
    elif symbol_one == symbol_two or symbol_one == symbol_three or symbol_two == symbol_three:
        win_amount = user_input * TWO_SCORE
        user_money += win_amount
        print("YOU WIN! $", win_amount, "\n")
    # If no symbals are the same, user loses amount entered, it is printed and subtracted from balance
    elif symbol_one != symbol_two and symbol_two != symbol_three:
        user_money -= user_input
        print("YOU LOSE $", user_input, "\n")
    
    # restarts process over by set of new random symbols and asking user to enter money
    randomize_choices()
    request_money()

main()