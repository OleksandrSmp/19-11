import zipfile

file_paths = ['student.py', 'group.py', 'main.py', 'human.py']
zip_name = 'project14-dz36.zip'

with zipfile.ZipFile(zip_name, 'w') as zip:
    for file in file_paths:
        zip.write(file)
print(f'Архив {zip_name} создан.')