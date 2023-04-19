# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input("Длина массива: "))
array = []

# рандомное число
# from random import randint
# array=[randint(1,10) for i in range(n)]
# print(array)

for i in range(n):
    num = int(input(f"Число {i+1}: "))
    array.append(num)
    # array.append(i)
print(f"Массив => {array}")

x = int(input("Введите число X: "))

# Ver_1
count = 0
for i in range(n):
    if array[i] == x:
        count += 1
if count == 0:
    print("Число Х отсутствует.")
else:
    print(f"Ответ: {count}")

# Ver_2
result2 = 0
for i in range(n):
    result2 = array.count(x)
print(f"Ответ (Ver_2): {result2}")

# Ver_3
result3 = [array[i] for i in range(n) if array[i] == x]
print(f"Ответ (Ver_3): {len(result3)}")
