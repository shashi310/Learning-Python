# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"

def longest_common_prefix(strs):
    if not strs:
        return ""

    # Sort the list of strings
    strs.sort()

    # Find the common prefix between the first and last strings
    prefix = ""
    for i in range(min(len(strs[0]), len(strs[-1]))):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]
        else:
            break

    return prefix

# Test the function
input_strings = ["flower", "flow", "flight"]
result = longest_common_prefix(input_strings)
print(result)  # Output: "fl"

# Time Complexity: O(m*n*log(n)), where m is the length of the shortest string and n is the number of strings in the list. Sorting takes O(n*log(n)) time, and finding the common prefix takes O(m) time.
# Space Complexity: O(m), where m is the length of the shortest string (space used for the prefix string).
