seconds = int(input("Введите количество секунд: "))
if seconds < 0 or seconds > 8639999:
    print("Ошибка! Введено неверное число секунд.")
else:
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    num = " "
    if days > 0:
        num += str(days) + " день "
    if hours < 10:
        num += "0"
    num += str(hours) + ":"
    if minutes < 10:
        num += "0"
    num += str(minutes) + ":"
    if seconds < 10:
        num += "0"
    num += str(seconds)
    print(num)
