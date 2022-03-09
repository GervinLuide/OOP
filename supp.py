#importisime vajalikud paketid
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "http://192.168.22.172/menu-example/"

requests_page = urlopen(url)
page_html = requests_page.read()
requests_page.close()
#saime infot veebilehelt

html_soup = BeautifulSoup(page_html, 'html.parser')

soogi_items = html_soup.find_all('li', class_="list-group-item")
#varastasime infot veebilehelt
soogid = []
for sook in soogi_items:
    soogi_items = []
    newstring = re.sub(r'[0-9, €]+', ' ', sook.text)
    soogid.append(newstring)
#panime tsükliga käima, stringiga printis laused
sook_items = html_soup.find_all('span', class_="label label-info pull-right")

hind = []
for sook1 in sook_items:
    title = sook1.find('span')
    hind.append(sook1.text)
#tsükli abil leidsime hinna
for i in range(len(soogid)):
    #panime kõik kokku
    print(soogid[i])
    print(hind[i])
