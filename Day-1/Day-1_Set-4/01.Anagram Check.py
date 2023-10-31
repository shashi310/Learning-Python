# 1. Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"

def are_anagrams(word1, word2):
    # Convert both words to lowercase and remove spaces
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    
    # Check if the sorted characters of both words are equal
    return sorted(word1) == sorted(word2)

# Test the function
result = are_anagrams("cinema", "iceman")
print(result)  # Output: True



# Time Complexity: O(n*log(n)) due to sorting operation,
# where n is the length of the longer input word.
# Space Complexity: O(n) for storing the sorted strings.
