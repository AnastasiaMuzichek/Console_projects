import time


def confirm(text: str) -> bool:
    w = input(text + '\nВведите 1 для согласия: ')
    if w == '1':
        return True
    else:
        print('Ну и считай в уме дальше!')
        return False


print('Привет! Это калькулятор!\n')
while confirm('Хотите что-то посчитать?'):
    try:
        x = float(input('Первое число: '))
        deystviye = input('Выберите действие и впишите ( + , - , * , / ):\n')

        y = float(input('Второе число: '))
        if deystviye == '+':
            print(x + y)
        elif deystviye == '-':
            print(x - y)
        elif deystviye == '*':
            print(x * y)
        elif deystviye == '/':
            if y != 0:
                print(x / y)
            else:
                print('На ноль делить нельзя!')
        else:
            print('Это не математическое действие!')
    except:
        print('Неккоректный ввод!')

    time.sleep(7)
