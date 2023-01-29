a = int(input('Введите пятизначное число:'))
b = 10000
x = 1000
y = 100
z = 10
left, right = divmod(a, b)
n, m = divmod(right, x)
n1, m1 = divmod(m, y)
n2, m2 = divmod(m1, z)
left, n, n1, n2, m2 = m2, n2, n1, n, left
a1 = (left * 10000 + n * 1000 + n1 * 100 + n2 * 10 + m2 * 1)
print(a1)
