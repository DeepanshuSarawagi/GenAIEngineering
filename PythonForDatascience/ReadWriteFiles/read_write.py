"""
An example to show how to read and write files in Python. We will write a text file, process its contents, and then read the processed data.
"""

with open('example.txt', 'w') as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("This is the third line.\n")

# Now let's read the file and process its contents
with open('example.txt', 'r') as file:
    lines = file.readlines()
    processed_lines = [line.strip().upper() for line in lines]
    print(processed_lines)