def prime_generator(end):
    diction = []
    for num in range(2, end):
        for num_1 in diction:
            if num % num_1 == 0:
                break
        else:
            diction.append(num)
            yield num
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(30)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')