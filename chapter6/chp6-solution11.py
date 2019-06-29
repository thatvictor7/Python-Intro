'''
Victor Montoya
Chapter 6 Solution 11
Prime Number List
28 June 2019
'''

def main():
    is_prime(4)

def is_prime(number):
    # print(number)
    if number % number != 0 and number % 1 == 0:
        print(number)

main()