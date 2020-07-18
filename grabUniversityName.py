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
            name.append(links.a.get_text().strip())
        except:
            continue

    name = name[1:-1]
    return name


def convertToLinkedIn(list):
    linkedIn = []

    for n in list:
        link = ""
        new_link = ""
        for l in n:
            if(l == " "):
                link += "%20"
            else:
                link += l
        new_link = "https://www.linkedin.com/search/results/all/?keywords=" + link + "%20business%20professor&origin=GLOBAL_SEARCH_HEADER"
        linkedIn.append(new_link)

    return linkedIn


print(convertToLinkedIn(getName()))
print("Lenght: ", len(convertToLinkedIn(getName())))
