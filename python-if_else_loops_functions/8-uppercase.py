#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # Kiçik hərfləri yoxlayırıq və onları böyük hərflərə çeviririk
        if 'a' <= c <= 'z':
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()  # Yeni xət
