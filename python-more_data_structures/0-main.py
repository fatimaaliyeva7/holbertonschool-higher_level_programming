#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list
my_list = [1, 2, 3, 4, 5]
# Test case 1: Print 2 elements from the list
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
# Test case 2: Print all elements from the list
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
# Test case 3: Print more elements than the list contains
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
