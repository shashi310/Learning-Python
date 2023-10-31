# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."


def safe_division(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
num1 = 5
num2 = 0

result = safe_division(num1, num2)
print(result)
