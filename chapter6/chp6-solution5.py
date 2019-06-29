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
    print("Seconds \t Meters")
    for iteration in range(MIN, MAX):
        print(float(iteration), "\t\t", falling_distance(iteration))

def falling_distance(time):
    distance = (MULTIPLIER * G) * (time ** POWER)
    return distance

main()
