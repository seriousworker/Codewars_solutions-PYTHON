def calculator(txt: str) -> str:
    spl = [i.count('.') for i in txt.split(' ')]
    oper = txt.split(' ')[1]
    calc = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '//': lambda x, y: x // y
            }
    return '.' * calc.get(oper)(spl[0], spl[2])


# def calculator(txt: str) -> str:
#     a, oper, b = txt.split()
#     op1 = len(a)
#     op2 = len(b)
#     return '.' * eval(f'{op1} {oper} {op2}')


if __name__ == '__main__':
    assert calculator("..... + ...............") == "...................."
    assert calculator("..... - ...") == ".."
    assert calculator("..... - .") == "...."
    assert calculator("..... * ...") == "..............."
    assert calculator("..... * ..") == ".........."
    assert calculator("..... // ..") == ".."
    assert calculator("..... // .") == "....."
    assert calculator(". // ..") == ""
    assert calculator(". - .") == ""


