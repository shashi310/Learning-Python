# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"


def fibonacci(n):
    if n <= 0:
        return "Please provide a positive integer."
    elif n == 1:
        return "0"
    elif n == 2:
        return "0 1"
    else:
        fib_sequence = ["0", "1"]
        for i in range(2, n):
            next_fib = int(fib_sequence[-1]) + int(fib_sequence[-2])
            fib_sequence.append(str(next_fib))
        return ' '.join(fib_sequence[:n])

# Test the function
n = 5
fib_sequence = fibonacci(n)
print(fib_sequence)
