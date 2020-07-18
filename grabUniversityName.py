import requests
from bs4 import BeautifulSoup

URL = "https://www.4icu.org/us/"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

def getName():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html5lib')
    name = []

    for links in soup.find_all("td"):
        try:
            # link.append(links.a.get('href'))
            # link.append(links.get_text().strip())
            print(links.a.get_text().strip())
            name.append(links.a.get_text().strip())
        except:
            continue

    name = name[1:-1]
    return name

print(getName())
