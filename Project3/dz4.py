a = float(input('Первое число:'))
x = input("Выберите действие: +, -, *, /, \n")
b = float(input('Второе число:'))
if x == '+':
    print(a + b)
elif x == '-':
    print(a - b)
elif x == '*':
    print(a * b)
elif x == '/':
    if b != 0:
        print(a / b)
    else:
        print("Неверная операция")












