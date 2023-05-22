# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9

def array(a: int, d: int, n: int) -> int:
    """Массив с арифметической прогрессией"""
    list = []
    for i in range(n):
        list.append(a+i*d)
    print(list)

a=int(input("Введите 1-ый элемент массива: "))
d=int(input("Введите разность: "))
n=int(input("Введите колличество элементов массива: "))
array(a,d,n)

# Ver_2
progression=[a + (i-1) * d for i in range(1,n+1)]
print(progression)