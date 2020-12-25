from requests import get
from bs4 import BeautifulSoup
response=get('https://dbkpop.com/db/all-k-pop-idols?fbclid=IwAR2MJ3lvDxL0f6zuG_wmnBKXEDFP3A4WlIWFUq0VaNUjWyzG_njNOgm1Hw4')
# file = open('kpop.html','w',encoding='utf8')
content_html = BeautifulSoup(response.text)
# file.write(content_html.prettify())
table=content_html.find('table',{'id':'table_1'})
need=table.find('tbody')
needall=need.find_all('tr')
a=needall[0]
# print(a)
x=(a.find('td'),{'class':'  column-full_name'})
print(x)
# for i in range(len(needall)):
#     a=needall[i].find('td',{'class':'  column-full_name'})
#     print(a)