import random

n = int(input())
m = int(input())

mas = []
if n == 0 or m == 0:
    print('Введите ненулевые значения')
else:
    for i in range(n):
        a = []
        for j in range(m):
            a.append(random.randint(1, 10))
        mas.append(a)
    for row in mas:
        print(row)

    maxstr = ''

    for elem in mas:
        maxstr += str(max(elem)) + ', '
    print(f'Максимумы в каждой строчке: {maxstr[:-2]}')
    maxstb = ''

    new_mas = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new_mas[j][i] = mas[i][j]

    maxstb = ''

    for elem in new_mas:
        maxstb += str(max(elem)) + ', '
    print(f'Максимумы в каждом столбце: {maxstb[:-2]}')

    summ1 = 0
    summ2 = 0
    for i in range(min(n, m)):
        summ1 += mas[i][i]
    print(f'Сумма диагонали: {summ1}')
    maxsum = 0
    for i in range(len(mas)):
        s = 0
        for el2 in mas[i]:
            s += el2
        if s > maxsum:
            k = i + 1
            c = mas[i]
            maxsum = s
    print(f'Наибольшая сумма {maxsum} в строке под номером {k} со значениями {c}')
