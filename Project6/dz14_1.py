number = int(input("Введите целое число больше нуля: "))
while number > 9:
    digits = [int(d) for d in str(number)]
    a = 1
    for digit in digits:
        a *= digit
    number = a
print(number)