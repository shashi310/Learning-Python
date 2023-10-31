def contains_duplicate(nums):
    """
    Checks if the given array contains any duplicates.
    
    Time Complexity: O(n), where n is the length of the input list.
    Space Complexity: O(n), where n is the length of the input list (space used for the set).
    """
    return len(nums) != len(set(nums))

# Test the function
input_list = [1, 2, 3, 1]
result = contains_duplicate(input_list)
print(result)  # Output: True
