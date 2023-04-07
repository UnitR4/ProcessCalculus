__autor__ = "Шарапов Владимир"

def SumCic(n:int, m:int):
    ''' Поиск суммы '''
    s = 0
    for i in range(1, n):
        for j in range(1,n):
            s += (1/(2*j+i))
    return s