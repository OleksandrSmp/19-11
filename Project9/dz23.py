def popular_words(text, words):
    words_in_text = text.lower().split()
    result_dict = {word: 0 for word in words}
    for word in words_in_text:
        if word in words:
            result_dict[word] += 1
    return result_dict
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
print('OK')