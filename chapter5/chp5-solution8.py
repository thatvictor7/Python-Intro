# Victor Montoya
# Chapter 5 Solution 8
# Celcius to Farenheit Table

# Declared constants for celcius to farenheit formula and the number of times t]the loop will be executed
FARENHEIT_MULTIPLIER = 1.8
FARENHEIT_ADDITION = 32
MAX_CELCIUS = 21

def main():
    iterator()

def iterator():
    # for loop will iterate from 0 to 21(MAX_CELCIUS)
    for num in range(MAX_CELCIUS):
        # pass number of iteration into another method as argument
        celcius_to_farenheit(float(num))

def celcius_to_farenheit(celcius_temp):
    # declared local variable that holds the covertion from celcius to farenheit
    results = (celcius_temp * FARENHEIT_MULTIPLIER) + FARENHEIT_ADDITION
    # passed results variable and original celcius temp variable to another method as argument
    display_results(results, celcius_temp)

def display_results(farenheit, celcius):
    # printed the arguments passed
    print(celcius, " \t ", farenheit)

main()