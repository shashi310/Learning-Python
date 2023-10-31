# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def is_palindrome(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word = ''.join(word.split()).lower()

    if cleaned_word == cleaned_word[::-1]:
        return True
    else:
        return False

# Example usage
input_word = "madam"

if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")
