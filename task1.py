# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую неотрицательную степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def degree_num(num, degree):
    if degree == 1:
        return num
    elif degree == 0:
        return 1
    else:
        return num * degree_num(num, degree - 1)


a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print(degree_num(a, b))
