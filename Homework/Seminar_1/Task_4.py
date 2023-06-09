# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10
#     7 -> "нельзя определить"

print("---Задача 4: Найти сколько журавликов сделал каждый ребенок.---")

# Version_1
total_toys = int(input("Введите колличество журавликов: "))
katja_toys = total_toys*2/3
petja_toys = (total_toys - katja_toys)/2
sereja_toys = petja_toys

if katja_toys == int(katja_toys) and petja_toys == int(petja_toys):
    print(
        f"Общее {(total_toys)} -> Петя = {petja_toys} Катя = {katja_toys} Сергей = {sereja_toys}")
else:
    print("нельзя определить")
print("---")

# Version_2
input("Version_2: press Enter...")
total_toys_2 = int(input("Введите колличество журавликов: "))
if total_toys_2 % 6 == 0:
    print(f"Общее {(total_toys_2)} -> Петя = {total_toys_2/6} Катя = {total_toys_2*2/3} Сергей = {total_toys_2/6}")
else:
    print("нельзя определить")