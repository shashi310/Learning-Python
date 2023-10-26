# Write a Python function that takes a string and returns the string in reverse order.


# str="string"

# ans=""

# for i in range(len(str) - 1, -1, -1):
#     ans+=str[i]

# print(ans)


# --------------------using function----------------------

def reverse_string(input_string):
    return input_string[::-1]

# Certainly! input_string[::-1] is a Python slicing technique used to reverse a string (or any sequence, like a list).
# The first colon : denotes the start of the slicing.
# The second colon : denotes the end of the slicing.
# The -1 denotes the step size. A step of -1 means the slicing goes in reverse.


reversed_text = reverse_string("Hello, world!")
print(reversed_text)


reversed_text = reverse_string([1,2,3,4,5,6,7,8])
print(reversed_text)
