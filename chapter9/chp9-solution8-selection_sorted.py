'''
Victor Montoya
Chapter 9 Solution 8
Sorting Benchmark
Selection Sort
13 July 2019
'''

SINGLE_SUB = 1
SINGLE_ADD = 1

array = [26, 45, 56, 12, 78, 74, 39, 22, 5, 90, 87, 32, 28, 11, 93, 62, 79, 53, 22, 51]

def main():
    print("Original order:")
    print(*array)
    selection_sort(array)
    
def selection_sort(arr):
    start_scan = 0
    count = 0
    while start_scan < len(arr) - SINGLE_SUB:
        min_index = start_scan
        min_value = arr[start_scan]
        index = start_scan + SINGLE_ADD
        while index < len(arr):
            if arr[index] < min_value:
                min_value = arr[index]
                min_index = index
            index = index + SINGLE_ADD
        arr[min_index] = arr[start_scan]
        arr[start_scan] = min_value
        start_scan = start_scan + SINGLE_ADD
        count = count + SINGLE_ADD
    print("Selection Sorted: ")
    print(*arr)
    print("Number of location swaps: ", count)

main()