'''
Victor Montoya
Chapter 9 Solution 8
Sorting Benchmark
Insertion Sort
13 July 2019
'''

SINGLE_SUB = 1
SINGLE_ADD = 1

array = [26, 45, 56, 12, 78, 74, 39, 22, 5, 90, 87, 32, 28, 11, 93, 62, 79, 53, 22, 51]

def main():
    print("Original order:")
    print(*array)
    insertion_sort(array)
    
def insertion_sort(arr):
    count = 0
    index = 1
    while index < len(arr):
        unsorted_value = arr[index]
        scan = index
        while scan > 0 and arr[scan - SINGLE_SUB] > unsorted_value:
            arr[scan] = arr[scan - SINGLE_SUB]
            scan = scan - SINGLE_SUB
        arr[scan] = unsorted_value
        count = count + SINGLE_ADD
        index = index + SINGLE_ADD
    print("Insertion Sorted: ")
    print(*arr)
    print("Number of location swaps: ", count)

main()