def common_elements():
    list1 = [i for i in range(3, 31, 3)]
    list2 = [i for i in range(5, 51, 5)]
    list_set = set(list1).intersection(set(list2))
    return list_set
print(common_elements())
