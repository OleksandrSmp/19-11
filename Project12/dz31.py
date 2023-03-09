import codecs
import re
def delete_html_tags(html_file, result_file = 'cleaned.txt'):
    with open(html_file, 'r', encoding = 'utf-8') as file:
        html = file.read()
        cleaned_text = re.sub('<.*?>', '', html)
    with open(result_file, 'w', encoding = 'utf-8') as file:
        file.write(cleaned_text)
        delete_html_tags('example.html', 'cleaned.txt')
    with open('cleaned.txt', 'r', encoding = 'utf-8') as file:
        cleaned_text = file.read()
    print(cleaned_text)










