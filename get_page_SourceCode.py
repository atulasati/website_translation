import requests
from bs4 import BeautifulSoup
import time
from deep_translator import GoogleTranslator
from newt import get_translate


def getdata(url):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
                }
        r = requests.get(url=url,headers=headers)
        return r.text

def get_href(html):
        soup = BeautifulSoup(html,'html.parser')
        link = { 'hrefs_with_http' : [],
                 'hrefs_without_http' : []
                 }
        
        for a in soup.find_all('a', href=True):
                h = a['href']
                if h.startswith('http'):
                        link['hrefs_with_http'].append(h)

                else:
                        link['hrefs_without_http'].append(h)    
        return link

url = "https://www.classcentral.com/"

def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        content = []
        for data in soup.find_all("div"):
                c = data.get_text()
                c.replace('\n', '')
                content.append(c)
        return content


html = getdata(url)
time.sleep(3)  
href = get_href(html=html)

get_translate(url,'index')
for h in range(5): #len(href['hrefs_with_http'])
        url = href['hrefs_with_http'][h]
        get_translate(url=url,i=h)

