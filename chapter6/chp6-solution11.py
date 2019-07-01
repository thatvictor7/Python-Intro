'''
Victor Montoya
Chapter 6 Solution 11
Prime Number List
28 June 2019
'''

# Constants to set up prime numbers
START = 0
EVEN = 0

# Constants that holds info for spacing and table
FORMAT_TWO_CHARS = 10
FORMAT_THREE_CHARS = 99
TABLE_LENGTH = 4
MOVE_TABLE_POSITION = 1

# Constants hold range of iterator for loop
MIN = 1
MAX = 100

def main():
    # print(is_prime(1))
    iterator()

def is_prime(num):
    # If number passed to function is greater than 0 it will check to see if it's prime
    if num > START:
        # For loops range is from 2 up to the number passed
        for i in range(2,num):
            # If there's an instance where number is divisble by index number, it will break loop as it's a composite number
            if (num % i) == EVEN:
                return False
                break
        # If not composite number is found, True will return as it is a prime number
        else:
            return True
    # If number is less than 0 it is not a prime number
    else:
        return False

def iterator():
    # Declared variable to hold the rows of numbers and count variable
    row = ""
    counter = 0
    
    # for loop with range starting at 1
    for i in range(MIN,MAX):
        # If statement will use is prime function to check each index number within range
        if(is_prime(i)):
            # If counter is equal to 5 or more, it will print row as it should be full and reset row variable and counter back to zero
            if counter > TABLE_LENGTH:
                print(row)
                row = ""
                counter = 0
            # If index is less than 10 it will add a space
            if i < FORMAT_TWO_CHARS:
                row += " "
                # If the range max is more than 99, it will add a spacer to keep numbers aligned
                if MAX > FORMAT_THREE_CHARS:
                    row += " "
            # If index is between 10 and 99 and max range is greater than 99 it will need a space to keep table numbers aligned
            if i > 9 and i < FORMAT_THREE_CHARS and MAX > FORMAT_THREE_CHARS:
                row += " "

            # Concatenates index number as string to row variable and a space after, adds 1 to counter
            row += str(i)
            row += " "
            counter += MOVE_TABLE_POSITION

main()