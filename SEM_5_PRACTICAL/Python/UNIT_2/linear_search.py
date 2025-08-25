# Program: Linear Search Implementation

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:   # check if element matches
            return i           # return index if found
    return -1                  # return -1 if not found

# Example usage
numbers = [10, 20, 30, 40, 50]
print("List:", numbers)

search_item = int(input("Enter the number to search: "))

result = linear_search(numbers, search_item)

if result != -1:
    print(f"Element {search_item} found at index {result}.")
else:
    print(f"Element {search_item} not found in the list.")
