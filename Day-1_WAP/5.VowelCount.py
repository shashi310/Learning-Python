# 6.  Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

#---------------my approach with right ans-------- 

# def VowelCount(str):
#     count=0
#     for i in range(len(str)):
#         if str[i] == "a" or str[i] == "e" or str[i] == "o" or str[i] == "u" or str[i] == "i":
#             count=count + 1
#     return count

# print( VowelCount("hellow"))


# -------------------new apporach-----------------


def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in input_string:
        if char in vowels:
            count += 1

    return count

# Test the function
input_string = "Hello"
num_vowels = count_vowels(input_string)
print(f"Number of vowels: {num_vowels}")
