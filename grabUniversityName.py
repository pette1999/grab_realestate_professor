import requests
from bs4 import BeautifulSoup

URL = "https://www.4icu.org/us/"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

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


def getCollegeLink():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html5lib')
    href = []

    for links in soup.find_all("td"):
        try:
            href.append("https://www.4icu.org/" + links.a.get('href'))
        except:
            continue

    href = href[1:-1]

    return href

def writeToFile(list):
    collegeLink = []
    collegeName = []
    file1 = open("collegeLink.txt", "a")
    file2 = open("collegeName.txt", "a")

    for l in list:
        page = requests.get(l)
        soup = BeautifulSoup(page.content, 'html5lib')

        for links in soup.find_all("td"):
            try:
                if(links.a.get('itemprop') == "url"):
                    collegeLink.append(links.a.get('href'))
                    file1.write(links.a.get('href') + "\n")
                    file1.close()
                    print(links.a.get('href'))

                    collegeName.append(links.a.span.get_text().strip())
                    file2.write(links.a.span.get_text().strip() + "\n")
                    file2.close()
                    print(links.a.span.get_text().strip())
            except:
                continue
    

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

# list = getCollegeLink()

# for i in list:
#     print(i)

writeToFile(getCollegeLink())