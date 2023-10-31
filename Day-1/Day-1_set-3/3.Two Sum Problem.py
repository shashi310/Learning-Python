# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"


def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i]
        
        num_indices[num] = i

    return None

# Example usage
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)

if result is not None:
    print(result)
else:
    print("No two elements sum up to the target.")
