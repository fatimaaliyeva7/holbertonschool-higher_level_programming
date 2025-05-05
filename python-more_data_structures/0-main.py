#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list  # funksiyanı import edirik
my_list = [1, 2, 3, 4, 5]
# Test 1: Listdən 2 element çap edirik
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))  # Çap olunan elementlərin sayını göstəririk
# Test 2: Listdəki bütün elementləri çap edirik
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
# Test 3: Listdə olan elementlərdən çoxunu çap etməyə çalışırıq
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
