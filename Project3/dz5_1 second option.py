lst = [1, 2, 3, 4, 5, 6]
lst1 = lst[:3]
lst2 = lst[3:]

# lst = [1, 2, 3]
# lst1 = lst[:2]
# lst2 = lst[2:]

# lst = []
# lst1 = lst[:1]
# lst2 = lst[1:]

if len(lst) == 3:
    print([lst1, lst2])
elif len(lst) == 6:
    print([lst1, lst2])
elif len(lst) == 0:
    print([lst1, lst2])
