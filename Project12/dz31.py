from bs4 import BeautifulSoup
import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
    num = BeautifulSoup(html, 'html.parser')
    cleaned_text = num.get_text()
    with codecs.open(result_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)
delete_html_tags('draft.html', 'cleaned.txt')












