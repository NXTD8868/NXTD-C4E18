from requests import get
from bs4 import BeautifulSoup

response = get('https://dantri.com.vn/')#get all info from inspect web
# file=open('dantri.html','w',encoding='utf-8')
# file.write(response.text)#create file with info from inspect web
content_html=BeautifulSoup(response.text)#LOAD UL TAG to bs4
ul_html=content_html.find('ul',{'class':'dt-list dt-list--link'})#find ul tag that contains data with class dt list...
li_html=ul_html.find_all('li')
for i in range(len(li_html)):
    a_html=(li_html[i].find('a'))
    print(a_html.text.strip())
    title=a_html.text.strip()
    link=a_html['href']
    print(link)
