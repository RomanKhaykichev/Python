# Information
*Python FLake 8 - ориентир  (скачать)*

**from random import randint** - рандомное число

**Flag**
```flag=False
 while not flag:
     coins =int(input("Error"))
     if not(coins==0 or coins==1):
         flag=True
```

**raise**-ошибка

___

| Тип коллекции | Создание |
|--------------:|---------------|
|1 Список       | *[ ], list( )*    |
|2 Кортеж       | *( ), tuple( )*   |
|3 Множество    | *{elm1,elm2}, set( )*|
|4 Неизменное множество| *frozenset( )* |
|5 Словарь      | *{ }, {key: value,} dict( )* |
>> list Comprehension - генератор списков

>> list_1 = [exp for item in iterable]

>>list_1 = [exp for item in iterable (if counditional)]

### **Для управления элементами списки имеют целый ряд методов. Некоторые из них:**

**append(item):** добавляет элемент item в конец списка

**insert(index, item):** добавляет элемент item в список по индексу index

**extend(items):** добавляет набор элементов items в конец списка

**remove(item):** удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError

**clear():** удаление всех элементов из списка

**index(item):** возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError

**pop([index]):** удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
**count(item):** возвращает количество вхождений элемента item в список

**sort([key]):** сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.

**reverse():** расставляет все элементы в списке в обратном порядке

**copy():** копирует список

### **Кроме того, Python предоставляет ряд встроенных функций для работы со списками:**

**len(list):** возвращает длину списка

**sorted(list, [key]):** возвращает отсортированный список

**min(list):** возвращает наименьший элемент списка

**max(list):** возвращает наибольший элемент списка
___

### Рекурсия и алгоритмы

>> Фибоначчи.
```
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i - 2))
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]
```

>> Быстрая сортировка
```
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))
```
>> Сортировка слиянием
```
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
```
