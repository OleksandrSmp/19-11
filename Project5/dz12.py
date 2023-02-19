import string
name = input('Type name: ')
punct = string.punctuation = ' '
name = name.title()
for i in punct:
    name = name.replace( i, '')
name = f'#{name}'
if len(name)>140:
    name = name[:140]
print(name)

