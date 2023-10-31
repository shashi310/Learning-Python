# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
#     - *Input*: "abc"
#     - *Output*: "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"

def permutations(s):
    """
    Calculates all permutations of a given string.
    
    Time Complexity: O(n!), where n is the length of the input string. This is because there are n! possible permutations.
    Space Complexity: O(n), where n is the length of the input string (space used for recursion stack and storing permutations).
    """
    if len(s) <= 1:
        return [s]
    
    result = []
    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i+1:]
        for p in permutations(remaining_chars):
            result.append(char + p)
    
    return result

# Test the function
input_string = "abc"
result = permutations(input_string)
print(result)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
