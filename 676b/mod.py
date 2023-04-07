__autor__ = "Шарапов Владимир"

import numpy as np

def CreateMatrix(n:int):
    ''' Создаем матрицу '''
    return np.random.randint(0,100, size = (n,n))

def PrintMatrix(a:np.array):
    ''' Вывод матрицы '''
    for i in range(0, len(a)):
        # a.shape -> массив из размерностей (по кол-ву столбцов)
        for j in range(0, a.shape[1]):          
            print(a[i][j], " ", end='')
        print()

def ColChange(a:np.array):
    ''' Меняем колонки местами по условию '''
    for i in range(len(a) // 2):
        a[i, :], a[len(a)-i-1, :] = a[len(a) - i - 1, :].copy(), a[i, :].copy()
    return a


