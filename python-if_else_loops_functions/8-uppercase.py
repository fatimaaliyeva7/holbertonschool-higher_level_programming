#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            # Kiçik hərfi böyük hərfə çevirmək üçün 32 çıxarırıq
            print(chr(ord(c) - 32), end="")
        else:
            # Böyük hərf və ya qeyri-hərf olanları olduğu kimi çap edirik
            print(c, end="")
    print()  # Yeni xətt
