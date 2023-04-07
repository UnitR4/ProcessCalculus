__autor__ = "Шарапов Владимир"

import math
import random

def CreareArrRand(n:int):
    ''' Функция рандомного создания элементов матрицы '''
    a = random.sample(range(100), n)
    return a

def CreateArray (n:int):
    ''' Функция создания матрицы '''
    a=[]
    for i in range(0,n):
        a.append(int(input("Введите число: ")))
    return a

def PrintArray(a:list):
    ''' Функция вывода матрицы '''
    for i in range(len(a)):
        print(f"{a[i]} ", end='')
    print()

def Result(a:list):
    ''' Функция вычесления задачи '''
    res = 0
    for i in range(len(a)):
        res += a[i]
    res = math.sin(abs(res))
    return res