# lst = [1, 2, 3, 4, 5, 6, 7, 9]
# lst = [1, 1, 1, 1]
# lst = [6, 3, 7]
import random
lst1 = [random.randint(1, 100) for i in range(random.randint(3, 10))]
print(lst1)
lst = ([lst1[0]] + [lst1[2]] + [lst1[-2]])
print(lst)

