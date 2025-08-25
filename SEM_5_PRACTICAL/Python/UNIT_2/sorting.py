# -------- Searching Functions --------
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i   # return index
    return -1          # if not found

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# -------- Sorting Functions --------
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

# -------- Menu Driven Program --------
def main():
    while True:
        print("\n--- Searching and Sorting Menu ---")
        print("1. Linear Search")
        print("2. Binary Search (Array must be sorted)")
        print("3. Selection Sort")
        print("4. Bubble Sort")
        print("5. Insertion Sort")
        print("6. Merge Sort")
        print("7. Quick Sort")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 8:
            print("Exiting... Goodbye!")
            break

        # Instead of map(), use simple method
        arr = []
        n = int(input("Enter how many numbers: "))
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            arr.append(num)

        if choice == 1:
            x = int(input("Enter element to search: "))
            index = linear_search(arr, x)
            if index != -1:
                print("Element found at index:", index)
            else:
                print("Element not found")

        elif choice == 2:
            arr.sort()  # Binary search needs sorted array
            print("Sorted Array:", arr)
            x = int(input("Enter element to search: "))
            index = binary_search(arr, x)
            if index != -1:
                print("Element found at index:", index)
            else:
                print("Element not found")

        elif choice == 3:
            selection_sort(arr)
            print("Sorted Array:", arr)

        elif choice == 4:
            bubble_sort(arr)
            print("Sorted Array:", arr)

        elif choice == 5:
            insertion_sort(arr)
            print("Sorted Array:", arr)

        elif choice == 6:
            merge_sort(arr)
            print("Sorted Array:", arr)

        elif choice == 7:
            quick_sort(arr, 0, len(arr)-1)
            print("Sorted Array:", arr)

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
