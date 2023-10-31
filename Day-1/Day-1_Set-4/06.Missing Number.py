# 6. **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#     - *Input*: [3, 0, 1]
#     - *Output*: "2"

def find_missing_number(nums):
    """
    Finds the missing number in an array of distinct numbers.
    
    Time Complexity: O(n), where n is the length of the input list.
    Space Complexity: O(1).
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Test the function
input_list = [3, 0, 1]
result = find_missing_number(input_list)
print(result)  # Output: 2
