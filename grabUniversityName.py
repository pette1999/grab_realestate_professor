import requests
from bs4 import BeautifulSoup

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
    links = []
    position = []
    count = 0
    info = []
    count2 = 0
    email = []
    address = []

    for i in soup.find_all('span'):
            try:
                # get link
                # if(i.get('class')[0] == 'block-content'):
                #     try:
                #         print("https://cee.stanford.edu" + i.a.get('href').strip())
                #         links.append("https://cee.stanford.edu" + i.a.get('href').strip())
                #         count += 1
                #     except:
                #         continue
                # if(i.get('class')[0] == 'social-media'):
                #     print(i.find_all('li')[1].a.get('href')[7:])
                # print(i.get('class'))


                # get link2
                # if(i.get('class') == ['first', 'last'] and count2 < 1):
                #     try:
                #         print(i.get_text().strip().split(" of ")[0])
                #         count += 1
                #         count2 += 1
                #     except:
                #         continue

                if(i.get('id') == 'lblcategory'):
                    try:
                        for m in i.find_all('a'):
                            print("https://olin.wustl.edu/EN-US/Faculty-Research/Faculty/Pages/" + m.get('href'))
                            count += 1
                    except:
                        continue

                # if(i.get('class') == ['directory_entry', 'grid']):
                #     try:
                #         print(i.a.get('href'))
                #         count += 1
                #     except:
                #         continue

                # if(i.get('class')[0] == 'value'):
                #     try:
                #         print(i.get_text().strip())
                #         count += 1
                #     except:
                #         continue

                # if(i.get('class')[0] == 'media-heading'):
                #     try:
                #         print(i.a.get('href'))
                #         count += 1
                #     except:
                #         continue

                # get name
                # if(i.get('class')[0] == 'block-content'):
                #     try:
                #         # print(i.p.strong.get_text().strip())
                #         print(i.h2.get_text().strip())
                #         has_major = True
                #         count += 1
                #     except:
                #         continue

                # get name2
                # if(i.get('class') == ['field-content', 'col-sm-8', 'col-xs-12', 's3-p-l0', 's3-m-b0', 's3-fs-3', 'pull-right']):
                #     count += 1
                #     print(i.a.get_text().strip())

                # get title
                # if(i.get('class')[0] == 'user-profile-title-block'):
                #     count += 1
                #     # print(i.get_text().strip())
                #     print(i.find_all("h3")[0].get_text().strip())

                # get title2
                # if(i.get('class') == ['field-content', 'col-sm-8', 'col-xs-12', 's3-p-l0', 'pull-right']):
                #     count += 1
                #     print(i.get_text().strip())

                # get phone number
                # if(i.get('id') == 'phone'):
                #     count += 1
                #     print(i.get_text().strip())

                # get phone2
                # if(i.get('class') == ['views-field', 'views-field-field-phone']):
                #     count += 1
                #     print(i.div.get_text().strip())

                # get email
                # if(i.get('class')[0] == 'title'):
                #     count += 1
                #     print(i.get_text().strip().split(" of ")[-1])

                #get email3
                # if(i.get('class') == ['views-field', 'views-field-field-secondary-email']):
                #     count += 1
                #     print(i.div.a.get_text().strip())

                # get email2
                # if(i.get('class') == ['field-content', 'col-sm-8', 'col-xs-12', 's3-p-l0', 'pull-right']):
                #     count += 1
                #     print(i.a.get_text().strip())

                # get address
                # if(i.get('id') == 'address'):
                #     count += 1
                #     print(i.get_text().strip())

                # get address2
                # if(i.get('class') == ['views-field', 'views-field-field-office-location']):
                #     count += 1
                #     print(i.div.get_text().strip())

                # get position
                # if(i.get('class') == ['views-field', 'views-field-field-position']):
                #     count += 1
                #     print(i.em.get_text().strip())

                # if(i.get('class')[0] == 'directory-row-column'):
                #     count += 1
                #     information = i.get_text().strip().replace(" ", "")
                #     print(information.split("\n"))
                #     position.append(information.split("\n"))
                # if(i.get('class')[0] == 'faculty-title'):
                #     count += 1
                #     # information = i.get_text().strip().replace("\t", " ")
                #     try:
                #         # print(information.split("\n")[-1].strip()[17:])
                #         print(i.get_text().strip())
                #     except:
                #         continue
            except:
                continue
        # for i in range(1, 126, 2):
        #     try:
        #         print(position[i][1])
        #     except:
        #         print(position[i][0])

    print(count)
    return links




def test3():
    college_links = []
    f = open("collegeLink.txt", "r")
    for i in f:
        print(i.replace("\n", ""))
        college_links.append(i.replace("\n", ""))

    email = []
    phone = []
    address = []
    position = []
    major = []
    info = []

    count = 0
    for i in college_links:
        page = requests.get(i, headers=headers)
        soup = BeautifulSoup(page.content, 'html5lib')

        # has_email = False
        # has_phone = False
        # has_address = False
        # has_position = False
        has_major = False
        count2 = 0
        count3 = 0

        for i in soup.find_all("span"):
            try:
                # email
                # if(i.get('class') == ['views-field', 'views-field-field-secondary-email']):
                #         count += 1
                #         has_email = True
                #         print(i.div.a.get_text().strip())
                
                # if(i.get('class')[0] == 'phone'):
                #     try:
                #         print(i.a.get_text().strip())
                #         count += 1
                #         has_major = True
                #     except:
                #         continue

                if(i.get('id') == 'mail' and count2 < 1):
                    try:
                        print(i.a.get_text().strip())
                        count += 1
                        count2 += 1
                        has_major = True
                    except:
                        continue

                


                # phone
                # if(i.get('id')[0] == "yui_3_17_2_1_1596264378351_460"):
                #     try:
                #         # for m in i.address.ul.find_all('li'):
                #         #     try:
                #         #         # if(m.span.get('class') == ['protect', 'hidden']):
                #         #         #     print(m.span.get_text().strip().replace("(through)", "@"))
                #         #         #     has_major = True
                #         #         #     count += 1
                #         #         if(m.a.get('class') == ['icon', 'tel']):
                #         #             print(m.a.get_text().strip())
                #         #             has_major = True
                #         #             count += 1
                #         #     except:
                #         #         continue
                #         address = i.find_all('address')[1].get_text().strip().replace(" ", "").split('\n')
                #         new_adr = ""
                #         for i in address:
                #             new_adr += i
                #             new_adr += " "
                #         print(new_adr)
                #         count += 1
                #         has_major = True
                #     except:
                #         continue
                        

                # address
                # if(i.get('class') == ['views-field', 'views-field-field-office']):
                #         count += 1
                #         has_address = True
                #         print(i.div.get_text().strip())
                # position
                # if(i.get('class')[0] == 'page-profile-detail__titles-list'):
                #     count += 1
                #     has_position = True
                #     has_major = True

                #     print(i.find_all("li")[-1].get_text().strip().split(", ")[0])
                #     position.append(i.find_all("li")[-1].get_text().strip().split(", ")[0])
                #     print(i.find_all("li")[-1].get_text().strip().split(", ")[-1])
                #     major.append(i.find_all("li")[-1].get_text().strip().split(", ")[-1])

                # if(i.get('class')[0] == 'contact-info'):
                #     has_email = True
                #     count += 1
                #     print("https://www.hbs.edu" + i.find_all('p')[3].a.get('href'))
                # if(i.get('class')[0] == 'faculty-title'):
                #     count += 1
                #     has_position = True
                #     try:
                #         print(i.get_text().strip())
                #     except:
                #         continue
                            
            except:
                continue

        if(has_major == False):
            count += 1
            print("no email")
            info.append("no phone")
    

    print(count)


# college_links = []
# f = open("collegeLink.txt", "r")
# for i in f:
#     print(i.replace("\n", ""))
#     college_links.append(i.replace("\n", ""))

# for i in college_links:
#     test(i)

# test("https://olin.wustl.edu/EN-US/Faculty-Research/Faculty/Pages/Academic-Areas.aspx")
test3()
