import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def getdata(url):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
                }
        r = requests.get(url=url,headers=headers)
        return r.text

def get_href(html):
        soup = BeautifulSoup(html,'html.parser')
        link = []
        
        for a in soup.find_all('a', href=True):
                h = a['href']
                if h.startswith('http'):
                        link.append(h)

                else:
                        link.append("https://www.classcentral.com"+h)
        return link


def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        content = []
        for data in soup.find_all("div"):
                c = data.get_text()
                c.replace('\n', '')
                content.append(c)
        return content

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
    file_path = f"/home/hp/Documents/translate_demo/templates/translated_{i}.html"
    with open(file_path, 'w') as f:
        f.write(translated_html)
        # print("file translated successfully.........!!!!!")




def start(count):
        url = "https://www.classcentral.com/"
        hrefs = [url]
        base_hrefs = get_href(html=getdata(url)) 
        hrefs.extend(base_hrefs)
        for href in range(count): 
                url = hrefs[href]
                get_translate(url=url,i=href)

