#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        if isinstance(i, int):  # Ensure the item is an integer
            print("{}".format(i))
        else:
            raise TypeError("All elements must be integers")
