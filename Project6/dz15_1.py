digit = int(input('Type seconds: '))
days, digit= divmod(digit, 60*60*24)
hours, second = divmod(digit, 60*60)
minutes, seconds = divmod(digit, 60)
if 5 < days < 21:
     days_str = "дней"
elif str(days)[-1] == '1':
     day_str = "день"
elif str(days)[-1] in ('234'):
     day_str = "дня"
else:
    day_str = "дней"
res = f'{days} {day_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}'
print(res)












