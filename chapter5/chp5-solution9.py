# Victor Montoya
# Chapter 5 Solution 9
# Pennies for Pay
DAY_ADDITION = 1
PAY_DOUBLER = 2

days = 0
current_pay = .01
running_total = .01

def main():
    display_program_and_obtain_days()
    iterator()

def display_program_and_obtain_days():
    global days
    print("How much money will you earn in a period of time if your starting pay is",
          " 1 penny on first day and doubles every day")
    days = int(input("Enter Number of Days: ")) + DAY_ADDITION

def iterator():
    print("Day \t  Pay \t\t\t Total")
    for day in range(1,days):
        calculate_and_display_results(day)

def calculate_and_display_results(day_number):
    global current_pay
    global running_total

    print(day_number, " \t ",current_pay, " \t \t", running_total)
    current_pay = current_pay * PAY_DOUBLER
    running_total += current_pay

main()