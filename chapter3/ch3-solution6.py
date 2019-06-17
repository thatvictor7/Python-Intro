#Chapter 3 solution 6
#Body Mass Index

#Created variable to save bmi what will be calculated with a function
bmi = 0

#Turned bmi variable into a global variable so it can be accessed throughout program.
#main function calls the request_weight function.
def main():
    global bmi
    request_weight()

#function displays message to user and gets an input back that's saved to variable
#then that variable gets printed in next line. The request_height() function
#gets called last in this function
def request_weight():
    weight = float(input("Enter a weight in lbs. "))
    print(weight,"lbs.")
    request_height(weight)

#function displays message and asks user for height that gets saved to height 
#variable. Height variable gets printed and last, calculate_bmi() function is called.
def request_height(weight):
    height = float(input("Enter a height in inches. "))
    print(height, "in.")
    calculate_bmi(height,weight)

#function receives 2 arguments, the height and weight variables, then it calculates
#the bmi by multiplying weight by 703 and diving it by height ^ height and saves to 
# bmi varaiable. It prints results in the last line.
def calculate_bmi(height, weight):
    bmi = (weight * 703) / (height ** 2)
    print(bmi)


main()
