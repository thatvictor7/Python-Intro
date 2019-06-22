# Victor Montoya
# Chapter 5 Solution 9
# Pennies for Pay

# Declared constants 
DAY_ADDITION = 1
PAY_DOUBLER = 2
STARTING_POINT = 1

# Declared variables that will hold input, current pay getting doubles and the addition of salary
days = 0
current_pay = .01
running_total = .01

def main():
    display_program_and_obtain_days()
    iterator()

def display_program_and_obtain_days():
    # Declared days as a global variable
    global days

    # Printed purpose of program
    print("How much money will you earn in a period of time if your starting pay is",
          " 1 penny on first day and doubles every day")
    # Value of days global variable will be an integer from user + 1 so the loop iterates from 1 to whatever user inputs
    days = int(input("Enter Number of Days: ")) + DAY_ADDITION

def iterator():
    # Print table headers
    print("Day \t  Pay \t\t\t Total")
    # For loop will iterate from 1 to whatever user entered
    for day in range(STARTING_POINT,days):
        # Inserted index into a function
        calculate_and_display_results(day)

def calculate_and_display_results(day_number):
    # Declared global variables
    global current_pay
    global running_total

    # Printing actual results
    print(day_number, " \t ",current_pay, " \t \t", running_total)
    # Doubles current pay value for next loop
    current_pay = current_pay * PAY_DOUBLER
    # Added current pay to accumulator
    running_total += current_pay

main()