# 4. Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"



# # Define the list of numbers
# numbers = [10, 20, 30, 40]

# # Calculate the sum
# sum_of_numbers = sum(numbers)

# # Calculate the average
# average_of_numbers = sum_of_numbers / len(numbers)

# # Print the results
# print(f"Sum: {sum_of_numbers}, Average: {average_of_numbers}")



# Define the list of numbers
numbers = [10, 20, 30, 40]

# Initialize sum_of_numbers to 0
sum_of_numbers = 0

# Iterate over the numbers and calculate the sum
for num in numbers:
    sum_of_numbers += num

# Calculate the average
average_of_numbers = sum_of_numbers / len(numbers)

# Print the results
print(f"Sum: {sum_of_numbers}, Average: {average_of_numbers}")


# for loop
# Define the list of numbers
# numbers = [10, 20, 30, 40]

# # Initialize sum_of_numbers to 0
# sum_of_numbers = 0

# # Iterate over the indices using range
# for i in range(len(numbers)):
#     sum_of_numbers += numbers[i]
