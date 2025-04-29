#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':  # Check if the character is a lowercase letter
            result += chr(ord(c) - 32)  # Convert the lowercase letter to uppercase
        else:
            result += c  # Keep other characters unchanged
    print(result)  # Print the result
