from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
import requests


def get_translate(url,i):
    headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
                    }
    response = requests.get(url,headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    print("Html page translation started================")
    exclude_tags = ['script', 'style', 'comment','meta']
    for tag in soup.find_all(lambda tag: tag.name not in exclude_tags):
        if tag.name in ['script', 'style','comment','meta']:
            continue
        else:
            
            try:

                if tag.contents:

                    for child in tag.contents:
                        if isinstance(child, str):

                            translated_text = GoogleTranslator(source='en', target='hi').translate(child)

                            child.replace_with(translated_text)

                else:
                    translated_text = GoogleTranslator(source='en', target='hi').translate(tag.get_text())

                    tag.string.replace_with(translated_text)

            except:
                pass
        

    translated_html = str(soup)
    with open(f'translated_{i}.html', 'w') as f:
        f.write(translated_html)
        print("file translated successfully.........!!!!!")


