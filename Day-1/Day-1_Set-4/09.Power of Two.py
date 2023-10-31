def is_power_of_two(n):
    """
    Checks if the given integer is a power of two.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if n <= 0:
        return False
    
    # If a number is a power of two, it will have only one bit set to 1 in its binary representation
    # and (n & (n-1)) will be 0.
    return n & (n - 1) == 0

# Test the function
number = 16
result = is_power_of_two(number)
print(result)  # Output: True
