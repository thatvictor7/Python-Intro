# Victor Montoya
# Chapter 5 Solution 10
# Largest and Smallest

# Declared sentinel constant.
END = -99

# Declared input variable.
user_input = None

def main():
    # Print purpose of program.
    print("This program will return the LARGEST and SMALLEST number entered.")
    iterator()

def iterator():
    # Declared user input as a global variable.
    global user_input

    # While loop has condition set to as long as user input not equal to -99, keep running.
    while user_input != END:
        # declares new varaible for user input.
        new_input = int(input("Enter a number OR -99 to QUIT,... "))
        # If user input equals -99, it will break loop.
        if new_input == END:
            print("GOOD-BYE")
            break
        # inserts new variable with with user input and global variable with user input from previous loop into function.
        display_result(user_input, new_input)
        # replaces global variable user input with the new input for next iteration.
        user_input = new_input


def display_result(number_one, number_two):
    # If it's first iteration, this condition should be true and will display number entered as lasrgest and smallest.
    if number_one == None:
        print("Largest: ", number_two, " Smallest: ", number_two)
    # Else if user input global greater than new input, display as user input global as largest.
    elif number_one > number_two:
        print("Largest: ", number_one, "Smallest: ", number_two)
    # Default new input displayed as largest.
    else:
        print("Largest: ", number_two, "Smallest: ", number_one)

main()