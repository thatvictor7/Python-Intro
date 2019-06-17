# Victor Montoya
# Chapter 4 Solution 11
# Time Calculator

# Declare constants for time unit with seconds values
SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

# Declare variables to store results
days = 0
hours = 0
minutes = 0
seconds = 0

def main():
    display_calculator_description()
    request_seconds()
    calculate_time()
    print_results(seconds,minutes,hours,days)

def display_calculator_description():
    # Displays Name of program and instructions
    print("Time Calculator")
    print("When asked, ")
    print("enter a number of seconds to determine the:")
    print("number of days (86400 seconds in a day)")
    print("number of hours (3600 seconds in a hour)")
    print("number of minutes (60 seconds in a minute)")
    print("remaining seconds.")

def request_seconds():
    # Declared seconds as a global variable
    global seconds

    # Obtained seconds from user
    seconds = int(input("Enter a number of seconds: "))

def calculate_time():
    # Declared global variables to store results
    global days
    global hours
    global minutes
    global seconds

    if seconds >= SECONDS_PER_DAY:
        # Reassign value of days global variable by taking seconds and dividing by SECONDS_PER_DAY (86400)
        days = (seconds // SECONDS_PER_DAY)
        # Subtract days in seconds from seconds global variable
        seconds -= days * SECONDS_PER_DAY
        if seconds >= SECONDS_PER_HOUR:
            # Reassign value of hours global variable by taking seconds and dividing by SECONDS_PER_HOUR (86400)
            hours = (seconds // SECONDS_PER_HOUR)
            # Subtract hours in seconds from seconds global variable
            seconds -= hours * SECONDS_PER_HOUR
            if seconds >= SECONDS_PER_MINUTE:
                # Reassign value of minutes global variable by taking seconds and dividing by SECONDS_PER_MINUTE (86400)
                minutes = (seconds // SECONDS_PER_MINUTE)
                # Subtract minutes in seconds from seconds global variable
                seconds -= minutes * SECONDS_PER_MINUTE
    elif seconds >= SECONDS_PER_HOUR:
        if seconds >= SECONDS_PER_HOUR:
            hours = (seconds // SECONDS_PER_HOUR)
            seconds -= hours * SECONDS_PER_HOUR
            if seconds >= SECONDS_PER_MINUTE:
                minutes = (seconds // SECONDS_PER_MINUTE)
                seconds -= minutes * SECONDS_PER_MINUTE
    else:
        if seconds >= SECONDS_PER_MINUTE:
            minutes = (seconds // SECONDS_PER_MINUTE)
            seconds -= minutes * SECONDS_PER_MINUTE

def print_results(secondsParam, minutesParam, hoursParam, daysParam):
    # Prints results from parameters
    print(daysParam, "day(s)")
    print(hoursParam, "hour(s)")
    print(minutesParam, "minute(s)")
    print(secondsParam,"second(s)")

main()
