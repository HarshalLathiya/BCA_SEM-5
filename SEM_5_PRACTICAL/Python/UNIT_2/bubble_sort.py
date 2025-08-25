# bubble_sort.py
# Program to implement Bubble Sort in Python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Number of passes
        for j in range(n - i - 1):  # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Main Program
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted List:", numbers)

bubble_sort(numbers)

print("Sorted List:", numbers)
