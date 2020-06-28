# Сделайте бенчмарк двух функций, в каждой из которых одна и та же цель:
# принимает на вход число и возвращает список чисел во второй, третье, четвертой и 5 степени.
# Одна функция делает это с помощью рекурсии, другая с помощью цикла.
# В результате бенчмарк сдавать в виде графика.
from simple_benchmark import benchmark
from matplotlib import pyplot


def cycle(number):
    lst = []
    for i in range(2, 6):
        ans = number ** i
        lst.append(ans)
    return lst


def recursion(number, powers=5):
    if powers == 2:
        return [number ** powers]

    else:
        rec = recursion(number, powers - 1)
        rec.append(number ** powers)
        return rec


func = [recursion, cycle]
arguments = {}
for i in range(50):
    arguments[f'i{i}'] = i
print(arguments)
arguments_name = 'natural numbers'
aliases = {cycle: "Циклическая функция", recursion: "Рекурсия"}


b = benchmark(func, arguments, arguments_name, function_aliases=aliases)
b.plot()
pyplot.savefig('powers_of_number.png')
pyplot.show(b)
