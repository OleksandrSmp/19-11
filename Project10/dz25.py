def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    yield begin
    for i in range(1, end):
        begin = func(begin)
        yield begin
assert list(some_gen(2, 4, pow)) == [2, 4, 16, 256], 'Test1'
assert list(some_gen(1, 5, lambda x: x * 3)) == [1, 3, 9, 27, 81], 'Test2'
print('OK')
