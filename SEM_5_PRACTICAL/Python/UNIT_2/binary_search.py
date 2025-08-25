# binary_search.py
# Program to implement Binary Search in Python

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Find middle index
        if arr[mid] == target:
            return mid   # Element found
        elif arr[mid] < target:
            low = mid + 1   # Search right half
        else:
            high = mid - 1  # Search left half
    return -1   # Element not found


# Main Program
numbers = [10, 20, 30, 40, 50, 60, 70]
print("List:", numbers)

item = int(input("Enter the number to search: "))

result = binary_search(numbers, item)

if result != -1:
    print(f"✅ Element found at index {result}")
else:
    print("❌ Element not found in the list")
