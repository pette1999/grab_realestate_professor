import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.4icu.org/us/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"}

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


def USC():
    page = requests.get(
        "https://www.marshall.usc.edu/faculty-research/faculty-directory", headers=headers)
    soup = BeautifulSoup(page.content, 'html5lib')

    name = []
    position = []
    link = []

    for i in soup.find_all('div'):
        try:
            # if(i.get('class')[0] == 'faculty_profile__information-name'):
            #     name.append(i.h4.a.get_text().strip())
            # if(i.get('class')[0] == 'faculty_profile__information-department'):
            #     position.append(i.get_text().strip())
            if(i.get('class')[0] == 'faculty_profile__information-name'):
                link.append("https://www.marshall.usc.edu" + i.h4.a.get('href').strip())
        except:
            continue
    
    return link
    
def USC2(links):
    email = []
    phone = []
    building = []
    room = []
    for i in links:
        page = requests.get(i, headers=headers)
        print(i)
        soup = BeautifulSoup(page.content, 'html5lib')

        has_email = False
        has_phone = False
        has_building = False
        has_room = False

        for i in soup.find_all('span'):
            try:
                if(i.get('class')[0] == 'icon-mail'):
                    has_email = True
                    email.append(i.div.div.a.get_text().strip())
                if(i.get('class')[0] == 'icon-phone'):
                    has_phone = True
                    phone.append(i.div.a.get_text().strip())
                if(i.get('class')[0] == 'directory_building'):
                    has_building = True
                    building.append(i.div.get_text().strip())
                if(i.get('class')[0] == 'directory_room'):
                    has_room = True
                    room.append(i.div.get_text().strip())
            except:
                continue
                
        if(has_email == False):
            email.append('no email')
        if(has_phone == False):
            phone.append('no phone')
        if(has_building == False):
            building.append('no bulding')
        if(has_room == False):
            room.append('no room')
        

    return email, phone, building, room


def test(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html5lib')

    count = 0
    info = []
    count2 = 0
    email = []
    address = []
    name = []
    links = []

    for i in soup.find_all('div'):
      try:
        if(i.get('class')[0] == 'col-md-4'):
          #name
          print(i.get_text().strip().split('\n')[0])
          count += 1
      except:
        continue

    print(count)
    return links




def test3():
    college_links = []
    f = open("collegeLink.txt", "r")
    for i in f:
        print(i.replace("\n", ""))
        college_links.append(i.replace("\n", ""))
    print('\n')
    email = []
    phone = []
    address = []
    position = []
    building = ""

    count = 0
    for i in college_links:
      if(i == "no link"):
          print(" ")
      else:
        page = requests.get(i, headers=headers)
        soup = BeautifulSoup(page.content, 'html5lib')

        has_major = False
        count2 = 0

        for i in soup.find_all("h2"):
          try:
            # if(i.get('class')[0] == 'headinfo' and count2 < 1):
            #   try:
            #     # title
            #     print(i.h2.get_text().strip())
            #     count += 1
            #     count2 += 1
            #     has_major = True
            #   except:
            #       continue
            print(i.get_text().strip())
          except:
            continue

        if(has_major == False):
          count += 1
          print("no address")
    

    print(count)


# college_links = []
# f = open("collegeLink.txt", "r")
# for i in f:
#     print(i.replace("\n", ""))
#     college_links.append(i.replace("\n", ""))

# for i in college_links:
#     print(i.split('/')[-1])

# test("https://www.nku.edu/academics/cob/programs/departments/management.html")
test3()
