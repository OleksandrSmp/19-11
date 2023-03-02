def prime_generator(end):
    primes = []
    for num in range(2, end):
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
            yield num
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(30)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')