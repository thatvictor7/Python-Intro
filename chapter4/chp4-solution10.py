# Victor Montoya
# Chapter 4 Solution 10
# Body Mass Index Program Enhancement

# Declared constant that will be used to calculate bmi and optimal range
BMI_MULTIPLIER = 703
MIN_OPTIMAL_RANGE = 18.5
MAX_OPTIMAL_RANGE = 25

# Declared global variables
bmi = 0
weight = 0
height = 0

def main():
    request_weight()
    request_height()
    calculate_bmi()
    calculate_bmi_optimal_range()

def request_weight():
    # Declare weight as global variable
    global weight

    # Obtain weight from user and assign it to weight variable
    weight = float(input("Enter a weight in lbs. "))

def request_height():
    # Declare height as global variable
    global height

    # Obtain height from user and assign it to height variable
    height = float(input("Enter a height in inches. "))

def calculate_bmi():
    # Declare bmi as global variable
    global bmi

    # Multiply weight by BMI_MULTIPLIER (703) and divide by height times height, assing result to bmi variable
    bmi = (weight * BMI_MULTIPLIER) / (height * height)

    # Print result
    print("Body Mass Index: ", bmi)

def calculate_bmi_optimal_range():
    # If bmi is within min and max optimal range it will print it is at optimal range
    if bmi >= MIN_OPTIMAL_RANGE and bmi <= MAX_OPTIMAL_RANGE:
        print("BMI is in the optimal range: 18.5 TO 25.0")

    # If bmi is greater than max optimal range it will print it's high from optimal
    elif bmi > MAX_OPTIMAL_RANGE:
        print("HIGH BMI - person is too short")
    # Any other bmi will be lower and display is lower from optimal
    else:
        print("LOW BMI - watch more TV")

main()