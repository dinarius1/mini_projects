one = int(input('Введите первое число: '))
two = int(input('Введите второе число: '))
operation = input('Выберите операцию из следующих: \n"+" - сложение \n"-" - вычитание \n"*" - умножение \n"/" - деление \n"%" - нахождение остатка \n"**" - возведение в степень \n"//" - целочисленное деление \nВыбранная операция: ')

if operation == '+':
    print(f'{one} + {two} = {one + two}')
elif operation == '-':
    print(f'{one} - {two} = {one - two}')
elif operation == '*':
    print(f'{one} * {two} = {one * two}')
elif operation == '/':
    print(f'{one} / {two} = {one / two}')
elif operation == '%':
    print(f'{one} % {two} = {one % two}')
elif operation == '**':
    print(f'{one} ** {two} = {one ** two}')
elif operation == '//':
    print(f'{one} // {two} = {one // two}')
else:
    print('Данной операции нет в системе')
