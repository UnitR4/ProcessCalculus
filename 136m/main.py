__autor__ = "Владимир Шарапов"

"""Задача 5: 136 Даны натуральное число n, действительные числа a1,..., an. Вычислить: буква м"""

import source

assert source.Result([2,4,6]) == -0.5365729180004349		# дописать аварийное завершение программы, если ответ не верен

n = int(input("Введите размер массива: "))
# a = source.CreateArray(n)
print("Данный массив: ")
a = source.CreareArrRand(n)
source.PrintArray(a)
print(f"Результат: {source.Result(a):.4f}")
