# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them again
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the function
input_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(input_list.copy())
print(sorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]

# Time Complexity: O(n^2) as we have nested loops iterating over the list,
# where n is the length of the list.
# Space Complexity: O(1) as we are not using any additional data structures.
