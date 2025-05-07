#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer
print(add_integer(1, 2))  # Expected: 3
print(add_integer(100, -2))  # Expected: 98
print(add_integer(2))  # Expected: 100 (since b defaults to 98)
print(add_integer(100.3, -2))  # Expected: 98 (100.3 is casted to 100)
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)  # Expected: "b must be an integer"
try:
    print(add_integer(None))
except Exception as e:
    print(e)  # Expected: "a must be an integer"
