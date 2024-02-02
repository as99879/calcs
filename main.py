num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
sign = input('Выберите операцию (Введите +, -, * или /): ')


def summa(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


if sign == '+':
    print(f'Сумма двух чисел:{summa(num1, num2)}')

if sign == '-':
    print(f'Разность двух чисел:{sub(num1, num2)}')

if sign == '*':
    print(f'Умножение двух чисел:{mult(num1, num2)}')

if sign == '/':
    print(f'Частное двух чисел:{div(num1, num2)}')

else:
    print("Такая операция отсутствует")
