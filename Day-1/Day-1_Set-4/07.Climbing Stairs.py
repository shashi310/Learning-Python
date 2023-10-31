# 7. **Climbing Stairs**: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#     - *Input*: 3
#     - *Output*: "3"

def climb_stairs(n):
    """
    Calculates the number of distinct ways to climb to the top of the stairs.
    
    Time Complexity: O(n), where n is the number of steps.
    Space Complexity: O(1).
    """
    if n == 1:
        return 1
    
    # Initialize variables for the first two steps
    first, second = 1, 2
    
    # Iterate through the remaining steps and calculate distinct ways
    for _ in range(3, n+1):
        current = first + second
        first, second = second, current
    
    return second

# Test the function
steps = 3
result = climb_stairs(steps)
print(result)  # Output: 3
