import codecs
import re
def delete_html_tags(html_file, result_file = 'cleaned.txt'):
    # Открываем файл для чтения
    with open(html_file, 'r', encoding = 'utf-8') as file:

        # Читаем текст из файла
        html = file.read()

        # Удаляем HTML-тэги
        cleaned_text = re.sub('<[^<]+?>', '', html)

        # Открываем файл для записи
    with open(result_file, 'w', encoding = 'utf-8') as file:
        # Записываем очищенный текст в файл
        file.write(cleaned_text)
delete_html_tags('draft.html', 'cleaned.txt')











