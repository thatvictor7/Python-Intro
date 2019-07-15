'''
Victor Montoya
Chapter 9 Solution 7
Seach Benchmark
14 July 2019
'''

# Constants hold values for loops and adding and subtracting
SINGLE_ADDITION = 1
SINGLE_SUBTRACTION = 1
SPLIT_HALF = 2
START = 0

array = [26, 45, 56, 12, 78, 74, 39, 22, 5, 90, 87, 32, 28, 11, 93, 62, 79, 53, 22, 51]

def main():
    print("Original order:")
    print(*array)
    bubble_sort(array)
    obtain_number()

def sequential_search(arr, value):
    # Loops through array checking each element until one matches, it will break at that point
    # and print result
    result = None
    for i in range(len(arr) ):
        if arr[i] == value:
            result = i + SINGLE_ADDITION
            break
    print("Sequential Search comparisons: ", result)
    print("The position of the number is ", result)

# This function searches for value, starting in the middle, if not found it will check to see if 
# value is above or below and go to that section. It will break in half again and again until found
# or return -1 if not found
def binary_search(arr, value):
    count = 0
    first = 0
    last = len(arr) - SINGLE_SUBTRACTION
    position = - 1
    found = False
    while not found and first <= last:
        middle = (first + last) // SPLIT_HALF
        if arr[middle] == value:
            count = count + SINGLE_ADDITION
            found = True
            position = middle + SINGLE_ADDITION
        elif arr[middle] > value:
            last = middle - SINGLE_SUBTRACTION
        else:
            count = count + SINGLE_ADDITION
            first = middle + SINGLE_ADDITION
    print("Binary search comparisons: ", count)
    print("The position of the number is ", position)

def bubble_sort(arr):
    count = 0
    max_element = len(arr) - SINGLE_SUBTRACTION
    while max_element >= START:
        index = 0
        while index <= max_element - SINGLE_SUBTRACTION:
            if arr[index] > arr[index + SINGLE_ADDITION]:
                temp = arr[index]
                arr[index] = arr[index + SINGLE_ADDITION]
                arr[index + SINGLE_ADDITION] = temp
                count = count + SINGLE_ADDITION
            index = index + SINGLE_ADDITION
        max_element = max_element - SINGLE_SUBTRACTION
    print("Bubble Sorted:")
    print(*arr)
    print("Number of location swaps: ", count)

def obtain_number():
    # Variable will hold users input and insert as argument to both functions
    user_input = int(input("Select a number in the Array to search for: "))
    sequential_search(array, user_input)
    binary_search(array, user_input)
    search_again()

def search_again():
    # Takes users input, if yes it will call function to start over, else it will exit program
    user_input = str(input("Do you want to search again? (Y=Yes)")).upper()
    if user_input == "Y" or user_input == "YES":
        obtain_number()
    else:
        exit
    



main()