# 37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.

# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Элементы последовательности вводятся на каждой строке.
# 1 2 3 4 -> 4 3 2 1

def reverse(n: int)->None:
    """Переворот строки рекурсией"""
    if n==0:
        return print("")
    k=input()
    reverse(n-1)
    return print(k)

n=int(input())
reverse(n)