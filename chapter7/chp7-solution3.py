'''
Victor Montoya
Chapter 7 Solution 3
Fat Gram Calculator
7 July 2019
'''

MULTIPLIER = 9
MIN = 0
TO_PERCENT = 100
LOW_FAT_LIMIT = 29

def main():
    print("This program calculates the % of calories from fat in a food,\n"
    "and signals when a food is low fat.\n",
    "When asked,...\n",
    "enter the number of fat grams and calories in the food.\n")
    obtainFatGrams()

def obtainFatGrams():
    user_input = float(input('Enter the number of fat grams (not less than 0.0 grams)\n'))

    while user_input <= MIN:
        user_input = float(input('Enter the number of fat grams (not less than 0.0 grams)\n'))

    obtainCalories(user_input)
    # return user_input

def obtainCalories(fat_grams):
    calories = fat_grams * MULTIPLIER
    input_string = 'Enter the number of calories (MUST exceed ' + str(calories) + ')\n'
    user_input = float(input(input_string))
    while calories > user_input:
        user_input = float(input(input_string))

    calculateFat(fat_grams, user_input)

def calculateFat(fat, calories):
    fat_percentage = ((fat * MULTIPLIER) / calories) * TO_PERCENT
    checkLowFat(fat_percentage)

def checkLowFat(percent):
    if percent > LOW_FAT_LIMIT:
        print('The percentage of fat in this food is ', percent, '%')
    else:
        print('This food is considered low fat because the percentage of fat: ', percent, '%, is below 30.0%')
    restart()

def restart():
    user_input = str(input("Press 'c' to continue OR 'q' to QUIT\n"))
    user_input = user_input.lower()
    if user_input == 'c':
        obtainFatGrams()
    elif user_input == 'q':
        exit()

main()
