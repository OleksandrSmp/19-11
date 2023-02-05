lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = []
lst1 = len(lst) // 2
a = lst[:lst1]
b = lst[lst1:]
lst2 = len(lst) // 2 + 1
d = lst[:lst2]
c = lst[lst2:]
lst_1 = len(lst)
f = lst[:lst_1]
g = lst[lst_1:]
if len(lst) == 6:
    print([a, b])
elif len(lst) == 3:
    print([d, c])
elif len(lst) == 0:
    print([f, g])

