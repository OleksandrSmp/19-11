a = int(input('Введите четырехзначное число:'))
x = 1000
y = 100
z = 10
left, right = divmod(a, x)
n, m = divmod(right, y)
n1, m1 = divmod(m, z)
print(left)
print(n)
print(n1)
print(m1)






