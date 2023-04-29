# 43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на одной строке через пробел.
# 1 2 1 3 4 5 3 4 -> 3
# 1 2 1 3 4 3 1 -> 2

# list_1 = (1, 2, 1, 3, 4, 5, 3, 4)
# list_2 = (1, 2, 1, 3, 4, 3, 1)

# Ver_1
def count_pair(array: list) -> int:
    """нахождение пар элементов из списка"""
    count = 0
    for i in set(array):
        numb = array.count(i)
        if numb > 1:
            count += numb//2
    return  count

list_1 = input("Введите 1-ый массив через пробел: ").split()
print(count_pair(list_1))

# Ver_2

pair_counter=sum(list_1.count(i)//2 for i in set(list_1))
print(pair_counter)
# print(count_pair(list_2))
