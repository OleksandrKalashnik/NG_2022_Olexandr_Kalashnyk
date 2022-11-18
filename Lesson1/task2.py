lang = 'RU'
lang_opt = input('Введите L, или любую клавишу, чтобы продолжить:  ')
f = 'Введите первое число:  '
o = 'Введите операцию (+,-, /, *):  '
s = 'Введите второе число:  '
r = 'Результат: '
e = 'Ошибка'
v = 'Введите "yes", чтобы продолжить, и любую клавишу, чтобы закончить:  '
start = 'yes'
while start == 'yes':
    a = float(input(f))
    operation = input(o)
    b = float(input(s))
    if operation == '+':
        print(r, a + b)
    elif operation == '-':
        print(r, a - b)
    elif operation == '/':
        print(r, a / b)
    elif operation == '*':
        print(r, a * b)
    else:
        print(e)
    start = input(v)