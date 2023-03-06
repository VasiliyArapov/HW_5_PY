# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def rec_sum(a, b, c=0):
    if c == a:
        return b
    return rec_sum(a, b, c + 1) + 1


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(rec_sum(a, b))