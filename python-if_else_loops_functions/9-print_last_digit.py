#!/usr/bin/python3
def print_last_digit(number):
    # If the number is negative, make it positive by using the absolute value
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
