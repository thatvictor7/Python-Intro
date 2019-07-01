'''
Victor Montoya
Chapter 6 Solution 5
Falling Distance
28 June 2019
'''

# Constant variables that hold values of formula.
G = 9.8
MULTIPLIER = .5
POWER = 2

# Min and Max constants for range of for loop.
MIN = 1
MAX = 11

def main():
    print("\nWelcome to the Falling Distance Calculator \n")
    iterator()

def iterator():
    # Prints table header
    print("Seconds \t Meters")
    # For loop starts at 1, ends at 10
    for i in range(MIN, MAX):
        # Passes second to function that calculates falling distance
        print(float(i), "\t\t", falling_distance(i))

def falling_distance(time):
    # Declared variable that holds formula with argument(seconds) and constants, returns results to be printed
    distance = (MULTIPLIER * G) * (time ** POWER)
    return distance

main()
