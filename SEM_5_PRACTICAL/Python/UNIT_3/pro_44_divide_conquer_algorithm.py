# Program: Divide and Conquer - Merge Sort Algorithm

def merge_sort(arr):
    if len(arr) <= 1:   # Base case: already sorted
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Conquer: Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Driver Code
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", arr)
sorted_arr = merge_sort(arr)
print("Sorted Array using Merge Sort:", sorted_arr)
