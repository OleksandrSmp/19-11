seconds = int(input("Введите количество секунд: "))
if seconds < 0 or seconds > 8639999:
    print("Ошибка! Введено неверное число секунд.")
else:
    days, seconds = divmod(seconds, 24*60*60)
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)
    result = f"{days} дней, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}" \
        if days > 0 else f"0 дней, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(result)





