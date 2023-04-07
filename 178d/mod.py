__autor__ = "Шарапов Владимир"

import math


def CreateArr(n:int):
    ''' Функция создания массива '''
    a = []
    for i in range(0,n):
        a.append(int(input("Введите число: ")))
    return a

def PrintArr(a:list):
    ''' Функция вывода массива '''
    for i in range(0, len(a)):
        print(a[i], " ", end='')
    print()

def FilterArr(a:list):
    ''' Функция поиска элементов удовлетворяющих условию 2k < ak < k!'''
    b = []
    for k in range(len(a)):
        if 2*(k+1) < a[k] < (k+1)*math.factorial(k+1):
            #print(a[k])
            b.append(a[k])
    return b