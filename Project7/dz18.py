def second_index(text, some_str):
    pass
    assert second_index("sims", "s")
    assert second_index("find the river", "e")
    assert second_index("hi", "h")
    assert second_index("Hello, hello", "lo")
    first_index = text.find(some_str)
    if first_index == -1:  # Если искомая строка не найдена
        return None
    second_index = text.find(some_str, first_index + 1)
    if second_index == -1:  # Если второе вхождение не найдено
        return None
    return second_index
    print('ОК')


