# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# С клавиатуры вводятся число монет и сами монеты построчно.

# Пример:
# Ввод: 1 1 1 1 0 0 -> 2

number_coins = int(input("Введите колличество монет: "))

# flag=False
# while not flag:
#     coins =int(input("Error"))
#     if not(coins==0 or coins==1):
#         flag=True


sum_eagle = 0
sum_tails = 0
for i in range(number_coins):
    coins = int(input(f"Монета {i+1}: "))
    if coins==0: sum_eagle +=1
    if coins==1: sum_tails +=1

if sum_eagle>sum_tails: print(f"Нужно перевернуть: {sum_eagle}")
if sum_eagle==sum_tails: print(f"Можно перевернуть монеты с решкой или гербом!")
else: print(f"Нужно перевернуть: {sum_tails}")
