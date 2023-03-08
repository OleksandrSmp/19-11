import codecs
import re
def delete_html_tags(html_file, result_file = 'cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        cleaned_text = re.sub('<.*?>', '', html)
        lines = filter(lambda x: x.strip(), cleaned_text.splitlines())
        cleaned_text = '\n'.join(lines)
    with codecs.open('cleaned.txt', 'r', 'utf-8') as file:
        cleaned_text = file.read()
    print(cleaned_text)







