def slovar(sl):
    d = {}
    for el in sl:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    return sorted(d.items(), key=lambda k: k[1], reverse=True)


slovo1 = input().lower()
slovo2 = input().lower()
mas = []
if len(slovo1) == 0 or len(slovo2) == 0:
    print('Введите строку')
else:
    for el in slovo1:
        if el in '0123456789!@#$%^&*()_+=-/.,<>"':
            slovo1 = slovo1.replace(el, '')
    for el in slovo2:
        if el in '0123456789!@#$%^&*()_+=-/.,<>"':
            slovo2 = slovo2.replace(el, '')

    cort1 = slovar(slovo1)
    cort2 = slovar(slovo2)

    for el1 in cort1:
        for el2 in cort2:
            if el1[1] == el2[1] and el2[0] not in mas:
                print(el1[0] + '=' + el2[0])
                mas.append(el2[0])
                break

    if len(mas) == 0:
        print('Нет букв, удовлетворяющих условию задачи')
    elif len(mas) != len(cort1) or len(mas) != len(cort2):
        print('Не у каждой буквы есть пара')
    elif len(mas) == len(cort1) and len(mas) == len(cort2):
        print('У каждой буквы есть пара')
