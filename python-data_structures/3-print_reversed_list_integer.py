def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    if isinstance(my_list, list):
        for i in reversed(my_list):
            if isinstance(i, int):
                print("{}".format(i))
