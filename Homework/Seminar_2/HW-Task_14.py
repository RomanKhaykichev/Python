# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
# не превосходящие числа N.

# Пример:
# Ввод: 13 -> 1, 2, 4, 8

n=int(input("Введите число: "))
i=0
while i**2<=n:
    print(2**i)
    i+=1