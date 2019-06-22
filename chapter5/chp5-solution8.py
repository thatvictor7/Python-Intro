# Victor Montoya
# Chapter 5 Solution 8
# Celcius to Farenheit Table

FARENHEIT_MULTIPLIER = 1.8
FARENHEIT_ADDITION = 32

def main():
    iterator()

def iterator():
    for num in range(21):
        celcius_to_farenheit(float(num))

def celcius_to_farenheit(celcius_temp):
    results = (celcius_temp * FARENHEIT_MULTIPLIER) + FARENHEIT_ADDITION
    display_results(results, celcius_temp)

def display_results(farenheit, celcius):
    print(celcius, " \t ", farenheit)
    # print(str(celcius), " \t ", str(farenheit))

main()