# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8 - рассматриваемый список
# 4 - начало диапазона
# 8 - конец
# Output:
# 2(7), 4(5), 5(8)


def find_index(list: list,start_num: int, end_num: int) -> int:
    """Определить индексы элементов массива в диапазоне"""
    for i in range(len(list)):
        if start_num<=list[i]<=end_num:
            print(f"{i}[{list[i]}]")

list = [1, 3, 7, 10, 5, 8]
start_num = 4
end_num = 8
print(list)
find_index(list,start_num,end_num)