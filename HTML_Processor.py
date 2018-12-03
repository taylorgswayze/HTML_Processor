import csv
from bs4 import BeautifulSoup

#LINKS
with open('links.csv', 'r') as link_csv:
    csv_reader = csv.reader(link_csv)
    links = list(csv_reader)

for i in links:
    counter = 0
    print(i[counter])
    counter += 1
    print(counter)


#INITIALIZE HTML FILE
html = open('4397_CAT_081618_Woodward.html', 'r+')
soup = BeautifulSoup(html, 'html.parser')




# WRAP CELLS
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
    i['bgcolor'] = 'FFCB08'
    i['valign'] = 'middle'
    i.img.replace_with('SHOP NOW')

print(soup.prettify())

html.close()

html = soup.prettify("utf-8")
with open('output.html', 'wb') as file:
    file.write(html)

print(links)