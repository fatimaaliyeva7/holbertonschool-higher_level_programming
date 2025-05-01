#!/usr/bin/python3

# calculator_1 faylından funksiyaları idxal edirik
import calculator_1

# a və b dəyişənlərini təyin edirik
a = 10
b = 5

# Hesablama əməliyyatlarını yerinə yetiririk və nəticələri çap edirik
if __name__ == "__main__":
    # Nəticələr: toplama, çıxma, vurma və bölmə
    result_add = calculator_1.add(a, b)
    result_sub = calculator_1.sub(a, b)
    result_mul = calculator_1.mul(a, b)
    result_div = calculator_1.div(a, b)

    # Formatlı şəkildə çap edirik
    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")
