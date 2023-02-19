import string
input_str = input("Введите две буквы через дефис: ")
min_letter, max_letter = input_str.split("-")
letters = string.ascii_letters
start_index = letters.index(min_letter)
end_index = letters.index(max_letter)
result = letters[start_index:end_index+1]
print(result)
