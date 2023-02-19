import keyword
import string
name = input('Type name: ')
punkt = string.punctuation.replace('_', '') + ' '
x = True
if name[0].isdigit():
    x = False
if name in keyword.kwlist:
    x = False
for i in punkt:
    if i in name:
        x = False
        break
if not name.islower():
    x = False
print(x)

