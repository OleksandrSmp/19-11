lst = [12, 3, 4, 10]
# lst = [1]
# lst = []
if lst:
    lst.insert(0, lst.pop())
    print(lst)
else:
    print(lst[:])
