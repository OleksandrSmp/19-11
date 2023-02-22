def add_one(digits):
    pass
    num = int(''.join(map(str, digits)))                           # Преобразуем список в число
    num += 1                                                       # Добавляем 1 к числу
    return [int(i) for i in str(num)]                              # Преобразуем результат обратно в список цифр
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9, 9]) == [1, 0, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
