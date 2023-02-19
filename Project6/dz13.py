import string
str = input("Введите две буквы через дефис: ")
min, max = str.split("-")
letters = string.ascii_letters
form1 = letters.index(min)
form2 = letters.index(max)
result = letters[form1 : form2 +1]
print(result)
