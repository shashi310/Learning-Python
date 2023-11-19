def print_rhombus(n):
    for i in range(n + 1):
        spaces = ' ' * (n - i)
        digits = ' '.join(map(str, range(i)))
        row = spaces + digits + str(i) + digits[::-1] + spaces
        print(row)

    for i in range(n - 1, -1, -1):
        spaces = ' ' * (n - i)
        digits = ' '.join(map(str, range(i)))
        row = spaces + digits + str(i) + digits[::-1] + spaces
        print(row)

# Example for n = 5
print_rhombus(5)

