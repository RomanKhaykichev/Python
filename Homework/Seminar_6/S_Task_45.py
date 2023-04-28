# 45. Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 10^5.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз(перестановка чисел новую пару не дает).
# Ввод: 1220
# Вывод:
# 220(1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110 сумма делителей равна 284) 284(1, 2... 142 сумма делителей равна 220)

# 1184 1210

k=1220

def friendly_number(num: int)->int:
  """нахождение дружественных чисел"""
  sum=0
  sum_1=0
  for i in k:
    for j in i:
      if i%j==0:
        sum+=j
    for i in sum:
        for j in i:
          if i%j==0:
            sum+=j
    if sum==sum_1:
      print(sum,sum_1)
      
friendly_number(k)
