from collections import Counter
from datetime import datetime
from time import sleep

# Task 1. Дан словарь.
# Создать новый словарь, поменяв местами ключ и значение.
dict_1 = {
    "фрукт": "апельсин",
    "овощь": "помидор",
    "ягода": "малина",
    "рыба": "щука",
    "мясо": "курица",
}
new_dict = {}

for key, value in dict_1.items():
    new_dict[value] = key

print(new_dict)

# Task 2. Создать функцию нахождения факториала.
# Variant 1
def factorial(n):
    """рекурсивная функция"""
    if n <= 0:
        return 1
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(10))

# Variant 2
def factorial2(n):
    """выводит список факториалов чисел в виде списка"""
    num = 1
    a = []
    for i in range(1, n + 1):
        num = num * i
        a.append(num)
    return a


print(factorial2(10))


# Variant 3
def factorial3(n):
    """нахождение факториала с помощью генератора"""
    number = 1
    for i in range(1, n + 1):
        number = number * i
        yield number


for i in factorial3(10):
    print(i, end=' ')

print()

# Task 3. Дан список чисел. Посчитать сколько раз встречается каждое число,
# используя функцию, для хранения данных использовать словарь.
# Variant 1
list_a = [2, 5, 8, 4, 3, 2, 8, 6, 5, 9, 5, 4, 3, 9, 1]
print(len(list_a))
list_b = [i for i in range(1, 16)]
print(list_b)
diction = dict(zip(list_b, list_a))
print(diction)
values = diction.values()
count = Counter(values)
print(dict(count))

# Variant 2
list_a = [2, 5, 8, 4, 3, 2, 8, 6, 5, 9, 5, 4, 3, 9, 1]
times = {}
for i in list_a:
    if i in times:
        times[i] += 1
    else:
        times[i] = 1

for key, value in times.items():
    print(f'{key}: {value},', end=' ')

print()

# Task 4. Создать функцию, которая будет вызываться из генератора списков и
# отдавать текущее время с задержкой в 1 секунду.
def time():
    n = int(input("Введите количество повторений: "))
    list_time = [i for i in range(1, n + 1)]
    for i in list_time:
        print(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        sleep(1)


print(time())
