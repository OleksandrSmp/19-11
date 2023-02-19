number = input('Введите целое число: ' )
if int(number)<=0:
    print(number)
else:
    a = 1
    while int(number) > 9:
        a *= int(number[-1])
        number = number[:-1]
    a *= int(number)
print(a)



