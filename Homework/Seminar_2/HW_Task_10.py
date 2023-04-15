# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# С клавиатуры вводятся число монет и сами монеты построчно.

# Пример:
# Ввод: 1 1 1 1 0 0 -> 2

number_coins = int(input("Введите колличество монет: "))

print("Введите 1 или 0, где решка=1, герб=0.")

sum_eagle = 0
sum_tails = 0
for i in range(number_coins):
    coins = int(input(f"Монета {i+1}: "))
    if coins == 0:
        sum_eagle += 1
    if coins == 1:
        sum_tails += 1

if sum_eagle < sum_tails:
    print(f"Нужно перевернуть {sum_eagle} монеты с гербом.")
if sum_eagle > sum_tails:
    print(f"Нужно перевернуть {sum_tails} монеты с решкой.")
if sum_eagle == sum_tails:
    print(f"Можно перевернуть {sum_eagle} монеты с решкой или {sum_tails} c гербом!")
