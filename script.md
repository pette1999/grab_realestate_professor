## University of Massachusetts Amherst
### Architecture
<code>
if(i.get('class')[0] == 'staff-title'):
    try:
        # name
        # print(i.a.get_text().strip())
        # profile Link
        # print("https://www.umass.edu" + i.a.get('href'))
        # title
        print(i.get_text().strip())
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class')[0] == 'staff-address' and count2 < 1):
    try:
        print(i.get_text().strip())
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>

### Business School
<code>
if(i.get('class')[0] == 'col-lg-6'):
    try:
        # name
        # print(i.get_text().strip())
        # link
        for m in i.find_all('a'):
            print(m.get('href'))
            count += 1
        # title
        # print(i.p.get_text().strip())
        # count += 1
    except:
        continue
</code>
<code>
if(i.get('class')[0] == 'prof-office' and count2 < 1):
    try:
        print(i.get_text().strip()[8:])
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>



## Oregon State University
### Business
<code>
if(i.get('class') == ['field-content', 'span3']):
    try:
        # name
        print(i.find_all('a')[0].get_text().strip() + " " + i.find_all('a')[1].get_text().strip())
        # title
        # print(i.get_text().strip().split('\n')[-1].strip())
        # link
        # print("https://business.oregonstate.edu" + i.a.get('href'))
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class')[0] == 'span9' and count2 < 1):
    # ['entity', 'entity-building', 'building-building', 'clearfix']
    try:
        # phone
        # index = i.get_text().strip().replace('\xa0', '').split('\n')[2].index("Office:")
        # print(i.get_text().strip().replace('\xa0','').split('\n')[2][index:][7:])
        # address
        # print(i.div.get_text().strip().split('\n')[0].strip())
        # email
        print(i.a.get('href'))
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>

### Engineering School
<code>
if(i.get('class') == ['views-field', 'views-field-field-contact-phone-office']):
    # ['views-field', 'views-field-field-contact-phone-office']
    # ['views-field', 'views-field-field-people-position-sub']
    try:
        # name
        # print(i.a.get_text().strip())
        # link
        # print(i.a.get('href'))
        # title
        # print(i.strong.get_text().strip())
        # email
        # print(i.a.get('href')[7:])
        # phone
        print(i.span.get_text().strip())
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class') == ['field', 'field-name-field-contact-building-name', 'field-type-text', 'field-label-hidden'] and count2 < 1):
    try:
        building = i.div.div.get_text().strip()
        print(building)
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>
<code>
if(i.get('class') == ['field', 'field-name-field-contact-physical-address', 'field-type-text', 'field-label-hidden'] and count2 < 2):
    try:
        print(building + " " + i.div.div.get_text().strip())
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>



## University of Houston
### Business School
<code>
if(i.get('cellspacing') == '0'):
    try:
        for m in i.tbody.find_all('tr'):
            try:
                # name
                # print(m.td.a.get_text().strip())
                # link
                # print("https://www.bauer.uh.edu/search/directory/" + m.td.a.get('href'))
                # phone
                # print(m.find_all('td')[2].get_text().strip())
                # department
                # print(m.find_all('td')[3].get_text().strip())
                # position
                # print(m.find_all('td')[1].get_text().strip())
                # Email
                # print(m.find_all('td')[4].a.get_text().strip())
                # Address
                print(m.find_all('td')[5].get_text().strip())
                count += 1
            except:
                continue
    except:
        continue
</code>

### Civil and Environment Engineering
<code>
if(i.get('class') == ['views-field', 'views-field-field-first-name']):
    try:
        # name
        # print(i.get_text().strip())
        # link
        # print("http://www.cive.uh.edu" + i.a.get('href'))
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class') == ['views-field', 'views-field-field-faculty-title'] and count2 < 1):
    try:
        # email
        # ['views-field', 'views-field-field-email']
        # print(i.div.span.get_text().strip().replace("[at]","@").replace("[dot]",".").replace(' ',''))
        # phone
        # ['views-field', 'views-field-field-phone']
        # print(i.div.get_text().strip())
        # address
        # ['views-field', 'views-field-field-office-location']
        # print(i.div.get_text().strip())
        # title
        print(i.div.get_text().strip())
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>



## George Mason University
### Business School
<code>
if(i.get('class')[0] == 'ml-profilelist-subitem'):
    try:
        # name
        # print(i.get_text().strip())
        # link
        # print("https://business.gmu.edu" + i.get('href'))
        # email
        print(i.a.get_text().strip())
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class')[0] == 'ml-profile-content' and count2 < 1):
    try:
        if(i.span.get_text().strip() == 'Office Location:'):
            print(i.find_all('span')[-1].get_text().strip())
            count += 1
            count2 += 1
            has_major = True
    except:
        continue
</code>

### Engineering School
<code>
if(i.get('class')[0] == 'info-data'):
    try:
        # name
        # print(i.get_text().strip())
        # link
        # print("https://volgenau.gmu.edu" + i.a.get('href'))
        # email
        # if("@" in i.get_text().strip()):
        #     print(i.get_text().strip())
        #     count += 1
        # phone
        if("-" in i.get_text().strip()):
            print(i.get_text().strip())
            count += 1
    except:
        continue
</code>
<code>
if(i.get('class')[0] == 'info-staff' and count2 < 1):
    try:
        # title
        # print(i.get_text().strip().split(",")[0])
        # count += 1
        # count += 1
        # has_major = True
        # address
        if("," in i.get_text().strip()):
            print(i.get_text().strip())
            count += 1
            count2 += 1
            has_major = True
    except:
        continue
</code>



## Colorado State University
### Business School
<code>
if(i.get('class') == ['user-listing-item', 'user-listing-phone']):
    try:
        # link
        # print("https://biz.colostate.edu" + i.div.a.get('href'))
        # title
        # print(i.get_text().strip())
        # email
        # print(i.a.get_text().strip())
        # phone
        print(i.get_text().strip())
        count += 1
    except:
        continue
</code>
<code>
if(i.get('itemprop') == 'worksFor' and count2 < 1):
    try:
        # phone
        # print(i.get_text().strip())
        # address
        # print(i.get_text().strip())
        # department
        print(i.get_text().strip().split(",")[0])
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>


### Civil and Environment Engineering
<code>
if(i.get('class')[0] == 'directory'):
    try:
        for m in i.tbody.find_all('tr'):
            try:
                print(m.find_all('td')[3].a.get_text().strip())
                count += 1
            except:
                continue
    except:
        continue
</code>
<code>
if(i.get('valign') == 'top' and count2 < 1):
    try:
        print(i.find_all('td')[1].p.get_text().strip().split('\n')[1][7:])
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>



## Brigham Young University
### Business School
<code>
if(i.get('class')[0] == 'individual'):
    try:
        # name
        # print(i.get_text().strip())
        # link
        # print("https://marriottschool.byu.edu" + i.get('href'))
        # title
        print(i.get_text().strip().split(",")[-2].strip())
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class') == ['main-content', 'msb-directory', 'content-style', 'col-xs-12', 'col-md-9'] and count2 < 1):
    try:
        for m in i.find_all('a'):
            try:
                print(i.get_text().strip())
                count += 1
                count2 += 1
                has_major = True
            except:
                continue
    except:
        continue
</code>



## Georgia State University
## Business School
<code>
if(i.get('class')[0] == 'profile'):
    try:
        # name
        # print(i.td.a.get_text().strip())
        # link
        # print(i.td.a.get('href'))
        # department
        # print(i.find_all('td')[2].a.get_text().strip())
        # title
        print(i.find_all('td')[1].get_text().strip().split(" of ")[0].split(" in ")[0])
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class')[0] == 'content-sidebar-wrap' and count2 < 1):
    try:
        print(i.aside.ul.find_all('li')[-1].span.get_text().strip()[8:])
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>



## University of Nebraska-Lincoln
### Business School
<code>
if(i.get('class')[0] == 'directory-name'):
    try:
        # name
        # print(i.a.get_text().strip())
        # link
        print("https://business.unl.edu" + i.a.get('href'))
        
        count += 1
    except:
        continue
</code>
<code>
if(i.get('style') == 'font-size:.9em; padding-bottom:10px;' and count2 < 1):
    try:
        # email
        # print(i.get_text().strip().split('\n')[-1].strip())
        # phone
        # print(i.get_text().strip().split('\n')[-4].strip())
        # address
        # print(i.get_text().strip().split('\n')[0].strip() + " " + i.get_text().strip().split('\n')[1].strip() + " " + i.get_text().strip().split('\n')[2].strip() + " " + i.get_text().strip().split('\n')[3].strip())
        # department
        # print(i.get_text().strip())
        # title
        print(i.get_text().strip().split('\n')[0].split(" of ")[0].split(" in ")[0])
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>

## Civil and Environment Engineering
<code>
if(i.get('class')[0] == 'eng-small-text'):
    try:
        # name
        # print(i.get_text().strip())
        # Link
        # print("https://engineering.unl.edu" + i.a.get('href'))
        # title
        # print(i.get_text().strip().split('\n')[-1].split(" of ")[-1].split(" in ")[-1])
        # email
        print(i.get_text().strip())
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class') == ['unl-font-sans', 'dcf-txt-sm'] and count2 < 1):
    try:
        # phone
        # print(i.div.div.get_text().strip())
        # address
        print(i.get_text().strip())
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>



## University of South Florida
### Business and Finance
<code>
if("mailto" in i.get('href') and count2 < 1):
    try:
        print(i.get_text().strip())
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
</code>



## University of Illinois at Chicago
### Business School
<code>
if(i.get('class')[0] == '_phone'):
    try:
        # name
        # print(i.a.get_text().strip().split('\n')[0].strip() + i.a.get_text().strip().split('\n')[1].strip())
        # link
        # print(i.a.get('href'))
        # title
        # print(i.get_text().strip())
        # email
        # print(i.a.get_text().strip())
        # phone
        print(i.a.get_text().strip())
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class') == ['_row', '-inline'] and count2 < 1):
    try:
        if("Building & Room:" in i.h2.get_text().strip()):
            print(i.p.get_text().strip())
            count += 1
            count2 += 1
            has_major = True
    except:
        continue
</code>

### Architecture
<code>
if(i.get('style') == 'text-align:center!important; background-color:none!important; color:black!important;'):
    try:
        # name
        # print(i.a.get_text().strip())
        # link
        print("https://arch.uic.edu" + i.a.get('href'))
        count += 1
    except:
        continue
</code>
<code>
if(i.get('class') == ['field', 'field-name-body', 'field-type-text-with-summary', 'field-label-hidden'] and count2 < 1):
    try:
        for m in i.div.div.find_all('p'):
            try:
                if("mailto" in m.a.get('href')):
                    print(m.a.get_text().strip())
                    count += 1
                    count2 += 1
                    has_major = True
            except:
                continue
    except:
        continue
</code>

## Civil Engineering
 - same as Business



 ## Rice Uniersity
 ### Business School
 <code>
 if(i.get('class')[0] == 'email-address'):
    try:
        # name
        # print(i.h4.get_text().strip())
        # link
        # print("https://business.rice.edu" + i.a.get('href'))
        # title
        # print(i.get_text().strip().split(" in ")[-1].split(" of ")[-1].split(" ")[0].strip())
        count += 1
    except:
        continue
 </code>
 <code>
 if(i.get('class')[0] == 'office' and count2 < 1):
    try:
        # email
        # print(i.a.get('href')[7:])
        # phone
        # print(i.get_text().strip())
        # address
        print(i.get_text().strip())
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
 </code>


 ### Architecture
 <code>
 if(i.get('class')[0] == 'job-title'):
    try:
        # name
        # print(i.h4.a.get_text().strip())
        # link
        # print("https://arch.rice.edu" + i.h4.a.get('href'))
        # title
        print(i.div.ul.li.get_text().strip())
        count += 1
    except:
        continue
 </code>
 <code>
 if(i.get('class')[0] == 'field-email' and count2 < 1):
    try:
        # email
        print(i.a.get('href')[7:])
        # phone
        # print(i.get_text().strip())
        # address
        # print(i.get_text().strip())
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
 </code>




 ## Temple University
 ### Business School
 <code>
 if(i.get('class')[0] == 'listing__dept'):
    try:
        # name
        # print(i.a.get_text().strip())
        # link
        # print(i.a.get('href'))
        # title
        # print(i.get_text().strip())
        # department
        print(i.get_text().strip())
        count += 1
    except:
        continue
 </code>
 <code>
 if(i.get('class')[0] == 'listing__contact' and count2 < 1):
    try:
        print(i.li.get_text().strip()[15:])
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
 </code>




 ## Syracuse University
 ### Architecture
 <code>
 if(i.get('class') == ['faculty_phone', 'col-sm-1']):
    try:
        # name
        # print(i.strong.a.get_text().strip())
        # link
        # print("https://soa.syr.edu" + i.strong.a.get('href'))
        # title
        # print(i.get_text().strip().replace("P/T","").strip())
        # email
        # print(i.a.get_text().strip())
        # Office
        # print(i.get_text().strip())
        # phone
        print(i.get_text().strip())
        count += 1
    except:
        continue
 </code>
 <code>
 if(i.get('id') == 'titleLB' and count2 < 1):
    try:
        print(i.get_text().strip().split('\n')[0].split(" of ")[-1].split(" in ")[-1])
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
 </code>




 ## The University of Oklahoma
 ### Business School
 <code>
 if(i.get('class')[0] == 'text'):
    try:
        # name
        # print(i.h4.get_text().strip())
        # title
        # print(i.find_all('p')[0].b.get_text().strip().split('\n')[0].split(" of ")[0].split(",")[0])
        # link
        # print("https://www.ou.edu" + i.find_all('p')[1].find_all('a')[1].get('href'))
        # email
        # print(i.find_all('p')[1].find_all('a')[0].get_text().strip())
        # phone
        # print(i.find_all('p')[1].get_text().strip().split('\n')[3][7:])
        # address
        print(i.find_all('p')[1].get_text().strip().split('\n')[2][8:])
        count += 1
    except:
        continue
 </code>



 ## The University of Oklahoma
 ## Business School
 <code>
 if(i.get('class') == ['col-xs-6', 'col-sm-3', 'col-sm-push-6', 'faculty-links']):
    try:
        # name
        # print(i.a.get_text().strip())
        # link
        # print("https://haslam.utk.edu" + i.a.get('href'))
        # title
        # print(i.get_text().strip()[12:].split(",")[0])
        # email
        for m in i.ul.li.find_all('a'):
            if("mailto" in m.get('href')):
                print(m.get_text().strip())
                count += 1
 </code>
 <code>
 if(i.get('class')[0] == 'f-cont-info' and count2 < 1):
    try:
        for m in i.find_all('a'):
            if("tel:" in m.get('href')):
                print(m.get_text().strip()[3:])
                count += 1
                count2 += 1
                has_major = True
    except:
        continue
 </code>



 ## University of Kansas
 ### Business School
 <code>
 if(i.get('class')[0] == 'name'):
    try:
        # name
        print(i.a.get_text().strip())
        # link
        # print("https://business.ku.edu" + i.a.get('href'))
        # title
        # print(i.get_text().strip())
        # email
        # print(i.get_text().strip())
        # phone
        # print(i.get_text().strip())
        # address
        # print(i.get_text().strip())
        count += 1
    except:
        continue
 </code>


 ### Architecture
 <code>
 if(i.get('class')[0] == 'building'):
    try:
        # name
        # print(i.span.a.get_text().strip())
        # link
        # print("http://architecture.ku.edu" + i.span.a.get('href'))
        # title
        # print(i.div.get_text().strip())
        # email
        # print(i.div.a.get_text().strip())
        # phone
        print(i.get_text().strip())
        count += 1
    except:
        continue
 </code>



 ## University of Cincinnati
 ### Business School
 <code>
 if(i.get('class') == ['component', 'text']):
    try:
        for m in i.find_all('p'):
            try:
                # name
                # print(m.a.get_text().strip())
                # link
                # print(m.a.get('href'))
                # title
                # print(m.get_text().strip().split('\n')[1].split(" of ")[0])
                # email
                # print(m.get_text().strip().split('\n')[2][7:])
                # phone
                # print(m.get_text().strip().split('\n')[-1][7:])
                # address
                print(m.get_text().strip().split('\n')[-2][8:])
                count += 1
            except:
                continue
    except:
        continue
 </code>



 ## Fordham University
 ### Business School
 <code>
 if(i.get('class') == ['editor', 'clearfix']):
    try:
        for m in i.find_all('p'):
            try:
                # name
                # print(m.a.strong.get_text().strip())
                # link
                # print("https://www.fordham.edu" + m.a.get('href'))
                # title
                # print(m.get_text().strip().split('\n')[1])
                # email
                print(m.get_text().strip().split('\n')[-1])
                count += 1
            except:
                continue
    except:
        continue
 </code>
 <code>
 if(i.get('class') == ['editor', 'clearfix'] and count2 < 1):
    try:
        # phone
        # print((i.find_all('p')[-2].get_text().strip().split('\n')[0] + i.find_all('p')[-2].get_text().strip().split('\n')[1] + i.find_all('p')[-2].get_text().strip().split('\n')[2])[20:])
        print(i.find_all('p')[-1].get_text().strip())
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
 </code>



 ## The University of Texas at Dallas
 ### Business School
 <code>
 if(i.get('class') == ['vcard-button', 'bt-primary']):
    try:
        # name
        # print(i.a.get_text().strip())
        # link
        # print("https://jindal.utdallas.edu" + i.a.get('href'))
        # title
        # print(i.get_text().strip())
        # email
        # print(i.get('href')[7:])
        # phone
        # print(i.get_text().strip())
        # address
        print(i.get_text().strip())
        count += 1
    except:
        continue
 </code>
 <code>
 if(i.get('class') == ['field', 'field-name-field-office', 'field-type-text', 'field-label-inline', 'clearfix'] and count2 < 1):
    try:
        # department
        print(i.get_text().strip()[8:])
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
 </code>



 ## University at Albany, State University of New York
 ### Business
 <code>
 if(i.get('class') == ['views-field', 'views-field-field-display-office-address']):
    try:
        # name
        # print(i.span.a.get_text().strip())
        # link
        # print("https://www.albany.edu" + i.span.a.get('href'))
        # title
        # print(i.div.get_text().strip())
        # email
        # print(i.div.a.get_text().strip())
        # address
        print(i.div.get_text().strip())
        count += 1
    except:
        continue
 </code>
 <code>
 if(i.get('class') == ['field', 'field--name-field-department-tax', 'field--type-entity-reference', 'field--label-hidden', 'field--items'] and count2 < 1):
    try:
        # title
        print(i.find_all('div')[-1].get_text().strip())
        # email
        # print(i.a.get_text().strip())
        # phone 
        # print(i.a.get_text().strip())
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
 </code>



 ## Western Michigan University
 ### Business School
 <code>
 if(i.get('class') == ['views-field', 'views-field-title']):
    try:
        # name
        # print(i.span.a.get_text().strip())
        # link
        print("https://wmich.edu" + i.span.a.get('href'))
        # title
        # print(i.div.get_text().strip().split(" of ")[0].split(" in ")[0])
        # department
        # print(i.div.get_text().strip().split(" of ")[-1].split(" in ")[-1])
        count += 1
    except:
        continue
 </code>
 <code>
 if(i.get('class') == ['field', 'field-name-field-phone-office', 'field-type-text', 'field-label-inline', 'inline', 'field-wrapper'] and count2 < 1):
    try:
        # email
        # print("https://wmich.edu" + i.div.div.a.get('href'))
        # phone
        print(i.span.get_text().strip())
        # address
        # print(i.get_text().strip()[10:])
        count += 1
        count2 += 1
        has_major = True
    except:
        continue
 </code>



 ## The University of Texas at Arlington
 ### Business School
 <code>
 if(i.get('id') == 'myTable'):
    try:
        for m in i.find_all('tr'):
            try:
                # name
                print(m.find_all('td')[1].strong.get_text().strip().split(',')[0])
                # link
                # print(m.find_all('td')[1].strong.a.get('href'))
                # title
                # print(m.find_all('td')[1].strong.get_text().strip().split(',')[-1].strip())
                # address
                # print(m.find_all('td')[1].get_text().strip().split('\n')[-1].strip())
                # phone
                # print(m.find_all('td')[2].a.get_text().strip())
                # email
                # print(m.find_all('td')[3].a.get_text().strip())
                count += 1
            except:
                print("")
                continue
    except:
        continue
 </code>



 ## Loyola University Chicago
 ### Business School
 <code>
 if(i.get('class')[0] == 'bold'):
    try:
        # name
        # print(i.a.get_text().strip())
        # link
        # print("https://www.luc.edu" + i.a.get('href'))
        # title
        # print(i.get_text().strip().split(',')[0].split(" of ")[0].split(" in ")[0])
        # address
        # print(i.get_text().strip())
        # phone
        # print(i.get_text().strip().split('\n')[0])
        # email
        index = i.get_text().strip().split('\n')[0].strip().index("'")
        # print(i.get_text().strip().split('\n')[2].strip()[index+1:-3].replace('&#64;','@').replace('&#46;','.'))
        print(i.get_text().strip().split('\n')[0].strip()[index+1:-3].replace('&#64;', '@').replace('&#46;', '.'))
        count += 1
    except:
        continue
 </code>



 ## University of Denver
 ### Business School
 <code>
 if(i.get('class')[0] == 'directory-office'):
    try:
        # name
        # print(i.a.get_text().strip().split(',')[0])
        # link
        # print(i.a.get('href'))
        # title
        # print(i.get_text().strip())
        # department
        # print(i.get_text().strip().split(" of ")[-1])
        # email
        # print(i.get('href')[7:])
        # phone
        # print(i.a.get_text().strip())
        # address
        print(i.get_text().strip())
        count += 1
    except:
        continue
 </code>