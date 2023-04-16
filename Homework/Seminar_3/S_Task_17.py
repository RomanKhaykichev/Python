# 17'. Дан список чисел. Определите,
# сколько в нем встречается различных чисел.
# [1, 2, 3, 4, 1, 2, 3]

nums = [1, 2, 3, 4, 1, 2, 3]
# print(len(set(nums)))

# кол-во чисел, встречающихся ровно 1 раз
result = []

for i in set(nums):
    if nums.count(i) == 1:
        result.append(i)
print(result, len(result))

result1 = [i for i in set(nums) if nums.count(i) == 1]
print(result1)