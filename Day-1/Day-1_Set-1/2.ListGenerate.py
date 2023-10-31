#3. Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
  #  - *Input*: None
  #  - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."


# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Add a number (20)
numbers.append(20)

# Remove a number (for example, 3)
numbers.remove(3)

# Sort the list
numbers.sort()

# Print the list
print(numbers)
