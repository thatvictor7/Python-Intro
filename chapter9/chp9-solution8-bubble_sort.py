'''
Victor Montoya
Chapter 9 Solution 8
Sorting Benchmark
Bubble Sort
13 July 2019
'''

SINGLE_SUB = 1
SINGLE_ADD = 1
START = 0

array = [26, 45, 56, 12, 78, 74, 39, 22, 5, 90, 87, 32, 28, 11, 93, 62, 79, 53, 22, 51]

def main():
    print("Original order:")
    print(*array)
    bubble_sort(array)

def bubble_sort(arr):
    count = 0
    max_element = len(arr) - SINGLE_SUB
    while max_element >= START:
        index = 0
        while index <= max_element - SINGLE_SUB:
            if arr[index] > arr[index + SINGLE_ADD]:
                temp = arr[index]
                arr[index] = arr[index + SINGLE_ADD]
                arr[index + SINGLE_ADD] = temp
                count = count + SINGLE_ADD
            index = index + SINGLE_ADD
        max_element = max_element - SINGLE_SUB
    print("Bubble Sorted:")
    print(*arr)
    print("Number of location swaps: ", count)

main()