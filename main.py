seconds = int(input("Введите число секунд: "))

days = seconds // (24 * 3600)
seconds = seconds % (24 * 3600)

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print("Время: {:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds))