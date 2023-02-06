lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = []
if len(lst) % 2 == 0:
    lst1 = len(lst) // 2
    print([lst[:lst1], lst[lst1:]])
elif len(lst) / 2 != 0:
    lst2 = len(lst) // 2 + 1
    print([lst[:lst2], lst[lst2:]])
else:
    print([lst[:], lst[:]])



