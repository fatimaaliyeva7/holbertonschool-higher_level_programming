#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Burada idx mənfi dəyərdirsə və ya idx siyahının uzunluğundan böyükdürsə
    # heç bir dəyişiklik etməyəcəyik
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Əgər idx düzgün qiymətdirsə, o zaman my_list-in həmin indeksindəki elementi dəyişirik
    my_list[idx] = element
    return my_list
