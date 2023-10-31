# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"


def count_words(input_file, output_file):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # Count the number of words
        word_count = len(content.split())

        # Write the count to the output file
        with open(output_file, 'w') as file:
            file.write(f'Number of words: {word_count}')

        print(f'Number of words counted and written to {output_file}.')

    except FileNotFoundError:
        print(f'File {input_file} not found.')

# Example usage
input_file = "input.txt"
output_file = "output.txt"

count_words(input_file, output_file)
