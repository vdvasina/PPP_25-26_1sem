def rec(vir):
    vir = vir.strip()
    if (vir[0] == '-' and vir[1:].isdigit()) or vir.isdigit():
        res = int(vir)
        return res
    if vir.startswith('(') and vir.endswith(')'):
        c = 0
        for i, j in enumerate(vir):
            if j == '(':
                c -= 1
            elif j == ')':
                c += 1
            if c == 0 and i != len(vir) - 1:
                break
        else:
            return rec(vir[1:-1])

    def f(vir, b):
        c = 0
        for i in range(len(vir) - 1, -1, -1):
            if vir[i] == '(':
                c -= 1
            elif vir[i] == ')':
                c += 1
            elif c == 0 and vir[i] in b:
                return i
        return -1


    index = f(vir, ['+', '-'])
    if index != -1:
        right = vir[index + 1:]
        left = vir[:index]
        oper = vir[index]
        right_v = rec(right)
        left_v = rec(left)
        if oper == '+':
            print(f'{left_v}{oper}{right_v}={left_v + right_v}')
            return left_v + right_v
        else:
            print(f'{left_v}{oper}{right_v}={left_v - right_v}')
            return left_v - right_v

    index = f(vir, ['*', '/'])
    if index != -1:
        right = vir[index + 1:]
        left = vir[:index]
        oper = vir[index]
        right_v = rec(right)
        left_v = rec(left)
        if oper == '/':
            print(f'{left_v}{oper}{right_v}={left_v / right_v}')
            return left_v / right_v
        else:
            print(f'{left_v}{oper}{right_v}={left_v * right_v}')
            return left_v * right_v

    raise ValueError(f"Некорректно {vir}")


k = input()
print(f'Итог: {rec(k)}')
