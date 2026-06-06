# File Reading and Writing Modes in Python

## Overview
This document provides a comprehensive reference for all file reading and writing modes available in Python.

## File Modes Reference

| Mode | Syntax | Description |
|------|--------|-------------|
| Read mode | `'r'` | Opens an existing file for reading. Raises an error if the file doesn't exist. |
| Write mode | `'w'` | Creates a new file for writing. Overwrites the file if it already exists. |
| Append mode | `'a'` | Opens a file for appending data. Creates the file if it doesn't exist. |
| Exclusive creation mode | `'x'` | Creates a new file for writing but raises an error if the file already exists. |
| Read binary mode | `'rb'` | Opens an existing binary file for reading. |
| Write binary mode | `'wb'` | Creates a new binary file for writing. |
| Append binary mode | `'ab'` | Opens a binary file for appending data. |
| Exclusive binary creation mode | `'xb'` | Creates a new binary file for writing but raises an error if it already exists. |
| Read text mode | `'rt'` | Opens an existing text file for reading. (Default for text files) |
| Write text mode | `'wt'` | Creates a new text file for writing. (Default for text files) |
| Append text mode | `'at'` | Opens a text file for appending data. (Default for text files) |
| Exclusive text creation mode | `'xt'` | Creates a new text file for writing but raises an error if it already exists. |
| Read and write mode | `'r+'` | Opens an existing file for both reading and writing. |
| Write and read mode | `'w+'` | Creates a new file for reading and writing. Overwrites the file if it already exists. |
| Append and read mode | `'a+'` | Opens a file for both appending and reading. Creates the file if it doesn't exist. |
| Exclusive creation and read/write mode | `'x+'` | Creates a new file for reading and writing but raises an error if it already exists. |

## Mode Breakdown

### Basic Modes
- **`'r'`** - Read only (default)
- **`'w'`** - Write only
- **`'a'`** - Append only
- **`'x'`** - Exclusive creation

### Binary vs Text
- Binary modes: `'rb'`, `'wb'`, `'ab'`, `'xb'`
- Text modes: `'rt'`, `'wt'`, `'at'`, `'xt'` (default)

### Read and Write Combinations
- **`'r+'`** - Read and write on existing file
- **`'w+'`** - Write and read (creates new file)
- **`'a+'`** - Append and read
- **`'x+'`** - Exclusive creation with read and write

## Usage Example

```python
# Read mode
with open('file.txt', 'r') as f:
    content = f.read()

# Write mode
with open('file.txt', 'w') as f:
    f.write('New content')

# Append mode
with open('file.txt', 'a') as f:
    f.write('Additional content')

# Read and write mode
with open('file.txt', 'r+') as f:
    content = f.read()
    f.write('More content')
```

