#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer
print("Case 1: [1, 2, 3]")
print_reversed_list_integer([1, 2, 3])
print("Case 2: [1]")
print_reversed_list_integer([1])
print("Case 3: []")
print_reversed_list_integer([])
print("Case 4: None")
print_reversed_list_integer(None)
print("Case 5: [1, 2, 'H', 9]")
print_reversed_list_integer([1, 2, "H", 9])
