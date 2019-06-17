# Victor Montoya
# Chapter 4 Solution 8
# Change for a Dollar Game

# Constants for coin values
PENNIES = .01
NICKELS = .05
DIMES = .10
QUARTERS = .25

# Global variable to keep track of users total input.
user_total = 0

def main():
    display_game()
    request_inputs()
    display_results()

def display_game():
    # Displayiing game title and description
    print("The Dollar Game")
    print("When asked, ")
    print("enter the number of pennies, nickels, dimes and quarters ")
    print("that will make EXACTLY one dollar.")

def request_inputs():
    # Declared variables for each coin type with value of the users input requested.
    # Next line of request calls calculate_coin_inputs function and inserts users input and
    # a the global constant for that type of coin.

    pennies = int(input("Enter the number of Pennies: "))
    calculate_coin_inputs(pennies, PENNIES)

    nickels = int(input("Enter the number of Nickels: "))
    calculate_coin_inputs(nickels, NICKELS)

    dimes = int(input("Enter the number of Dimes: "))
    calculate_coin_inputs(dimes, DIMES)

    quarters = int(input("Enter the number of Quartes: "))
    calculate_coin_inputs(quarters, QUARTERS)

def calculate_coin_inputs(coint_type, coin_values):
    # Declare user_total as a global variable.
    global user_total

    # Declare new variable total to equal coin_type parameter (which is user input) multiplied
    # by coin_values (one of the constants passed depending on coin type).
    total = coint_type * coin_values
    
    # Adds the coin total to the user_total global variable.
    user_total += total

def display_results():
    # First expression checks if user_total equals 1.00, if true it congratulates user.
    if user_total == 1.00:
        print("CONGRATULATIONS! You entered exactly $", round(user_total,2), "worth of coins.")
    # Second expression checks if user_total is greater than 1.00, prints they went over to user.
    elif user_total > 1.00:
        print("Sorry you went OVER with $", round(user_total,2), "worth of coins.")
    # Last expression is default, prints to user they're under.
    else:
        print("Sorry you only entered $", round(user_total,2), "worth of coins.")

    

main()