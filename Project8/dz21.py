def is_palindrome(text):
    clean_text = ''
    for char in text:
        if char.isalnum():
            clean_text += char.lower()
    return clean_text == clean_text[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
print("ОК")
