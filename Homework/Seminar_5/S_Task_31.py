# 31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи|

def fib(n:int)->int:   
    """n - ое число Фибоначчи"""
    if n in [1,2]:
        return 1
    return fib(n-1)+fib(n-2)

n=7
print(f"Фибоначчи '{n}' -> {fib(n)}")

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1) 