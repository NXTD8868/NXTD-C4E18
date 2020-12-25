from requests import get
from bs4 import BeautifulSoup
response= get('https://dantri.com.vn/')
content_html=BeautifulSoup(response.text)
ul = content_html.find('ul',{'class':'dt-list dt-list--lg'})
li = ul.find_all('li')
data=[]
for i in range(len(li)):
    a_html=li[i].find('a')
    title=a_html.text.strip()
    link=a_html['href']
    print(title)
    print(link)