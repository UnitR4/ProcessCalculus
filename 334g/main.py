# https://ivtipm.github.io/Programming/Glava10/index10.htm#z334

__autor__ = "Шарапов Владимир"

import mod

# Тесты
assert mod.SumCic(5,2) == 2.4488455988455993
assert mod.SumCic(100,20) == 90.86510126723813
assert mod.SumCic(20,100) == 15.699048555950986

# Ввод значение
n = int(input("Введите кол-во итераций в 1 цикле: "))
m = int(input("Введите кол-во итераций во 2 цикле: "))
# Поиск суммы
s = mod.SumCic(n,m)
print(f"Результат: {s}")
