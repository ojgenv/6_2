"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""

n = int(input('Введите число '))
x = 1
i = 0
while (i <= n):
    print(x)
    x *= 2
    i += 1