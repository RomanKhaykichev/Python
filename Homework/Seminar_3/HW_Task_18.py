# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Длина массива: "))
array = list()
result = []

for i in range(n):
    num = int(input(f"Число {i+1}: "))
    array.append(num)
print(array)

x = int(input("Введите Х: "))

# Ver_1
dif = max(array)
for i in range(len(array)):
    if x-array[i] >= 0 and dif >= x-array[i]:
        dif = x-array[i]
        result = array[i]
    if x-array[i] < 0 and dif >= array[i]-x:
        dif = array[i]-x
        result = array[i]
print(f"Ответ (Ver_1): {result}")

# Ver_2
result2=[array[i] for i in range(len(array))
         if x-array[i] >= 0 and dif >= x-array[i]
         or x-array[i] < 0 and dif >= array[i]-x]
print(f"Ответ (Ver_2): {result2}")