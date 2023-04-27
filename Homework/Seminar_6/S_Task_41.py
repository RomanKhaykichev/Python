# 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Массив чисел вводится в одну строку через пробел. Массив состоит из целых чисел.
# Пример:
# 5 1 3 7 9 6 -> 1
# 3 4 3 6 5 8 7 -> 3

array_1 = input("Введите массив через пробел: ").split()

def count_exlusive(array: list) -> int:
    """колличество элементов > сосодних в элементе"""
    count = 0
    for i in range(1, len(array)-1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            # if array[i]<array[i+1]>array[i+2]: //for i in range(len(array)-2):
            count += 1
    return count

print(array_1)
print(count_exlusive(array_1))
