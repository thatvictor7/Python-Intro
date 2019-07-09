'''
Victor Montoya
Chapter 7 Solution 1
Payroll Program with Input Validation
3 July 2019
'''

MIN_PAY_RATE = 7.5
MAX_PAY_RATE = 18.25

MIN_HOURS = 0
MAX_HOURS = 40

def main():
    pay = payRateValidator()
    hours = hoursValidator()
    displayResults(pay,hours)

def payRateValidator():
    user_input = float(input('Enter the pay rate (between 7.5 AND 18.25): \n'))

    while user_input < MIN_PAY_RATE or user_input > MAX_PAY_RATE:
        user_input = float(input('Enter the pay rate (between 7.5 AND 18.25): \n'))
    
    return user_input

def hoursValidator():
    user_input = float(input('Enter hours (between 0.0 AND 40.0): \n'))

    while user_input < MIN_HOURS or user_input > MAX_HOURS:
        user_input = float(input('Enter hours (between 0.0 AND 40.0):  \n'))

    return user_input

def displayResults(rate, hours):
    results = rate * hours
    print('\nGross Pay is: $', results)

main()