lst = [0, 1, 0, 3, 12]
# lst = [0]
# lst = [1, 0, 3, 0, 0, 0, 5]
# lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
lst1 = []
lst2 = []
for i in range(len(lst)):
    if lst[i] != 0:
        lst1.append(lst[i])
    else:
        lst2.append(lst[i])
print(lst1 + lst2)


