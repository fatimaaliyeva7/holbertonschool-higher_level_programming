#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)  # Convert lowercase to uppercase
        else:
            result += c  # Add other characters as is
    print(result)  # Print the final result in one go
