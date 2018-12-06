import csv
from bs4 import BeautifulSoup





filename = 'CAT-US-20181207-BMSMChris.html'

#INITIALIZE HTML FILE
html = open(filename, 'r+')
soup = BeautifulSoup(html, 'html.parser')

# WRAP ROWS
for i in soup.find_all('tr'):
    i.wrap(soup.new_tag('table'))



#displayblock images
for i in soup.find_all('img'):
    i['style'] = 'display:block;'

# TABLE FORMATTING
for i in soup.find_all('table'):
    i['border'] = '0'
    i['cellpadding'] = '0'
    i['cellborder'] = '0'
    i['align'] = 'center'
    i['valign'] = 'top'
    i['style'] = 'border-collapse:collapse;font-family:arial,helvetica,sans-serif;font-weight:bold;color:#000001;'
    i['cellpadding'] = '0'

# CELL FORMATTING
for i in soup.find_all('td'):
    i['height'] = i.img['height']
    i['width'] = i.img['width']
    i['border'] = '0'
    i['cellpadding'] = '0'
    i['cellborder'] = '0'
    i['align'] = 'center'
    i['valign'] = 'top'
    i['bgcolor'] = '000001'
    i['style'] = 'border-collapse:collapse;font-size:16px;'
    i['cellpadding'] = '0'

# CTA FORMATTING
for i in soup.find_all(id="CTA"):
    i['bgcolor'] = 'ffcb08'
    i['valign'] = 'middle'
    i.img.replace_with('SHOP NOW')
    i['style'] = 'color:#000001;'

# TEXT AREA FORMATTING
for i in soup.find_all(id="TEXT"):
    i['bgcolor'] = 'FFFFFF'


print(soup.prettify())

html.close()

html = soup.prettify("utf-8")
with open(filename, 'wb') as file:
   file.write(html)


