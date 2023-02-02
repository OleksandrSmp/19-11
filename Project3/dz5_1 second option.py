lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = []

lst1 = lst[:3]
lst2 = lst[3:]

lst3 = lst[:2]
lst4 = lst[2:]

if len(lst) == 6:
    print([lst1, lst2])
elif len(lst) == 3:
    print([lst3, lst4])
elif len(lst) == 0:
    print([lst3, lst4])
