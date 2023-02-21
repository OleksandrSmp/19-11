def second_index(text, num_str):
    num1 = text.find(num_str)
    if num1 == -1:
        return None
    second = text.find(num_str, num1 + 1)
    if second == -1:
        return None
    return second
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") == None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')


