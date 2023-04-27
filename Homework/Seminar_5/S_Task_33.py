# 33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# [1, 2, 3, 1, 2, 1, 5, 4, 5] -> [1, 2, 3, 1, 2, 1, 1, 4, 1]

list = [1, 2, 3, 1, 2, 1, 5, 4, 5]

# Ver_1
def replace(list):
    new_list = []
    for i in list:
        if i == 5:
            new_list.append(1)
        else:
            new_list.append(i)
    return new_list

# Ver_2
def replace_2(list):
    for i in range(len(list)):
        if list[i] == 5:
            list[i] = 1
    return list


print(list)
print(replace(list))
print(replace_2(list))