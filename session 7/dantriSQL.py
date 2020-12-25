from requests import get
from bs4 import BeautifulSoup
import pymysql
client=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Thaiduong8868'
)
board=client.cursor() 

def create_database():
    board.execute('CREATE DATABASE `DANTRISQL`')
def create_board():
    board.execute('''CREATE TABLE `DANTRISQL`.`linktittle`(
        tittle text(255),
        link text(255)
    )''')        
def insert_row(a,b):
    board.execute(f'''
    INSERT INTO `DANTRISQL`.`linktittle`(
        tittle,
        link
    ) VALUES (
        '{a}',
        '{b}'
    )''')
response = get('https://dantri.com.vn/')

content_html=BeautifulSoup(response.text)#LOAD UL TAG to bs4
ul_html=content_html.find('ul',{'class':'dt-list dt-list--link'})#find ul tag that contains data with class dt list...
li_html=ul_html.find_all('li')
# create_database()
# create_board()
for i in range(len(li_html)):
    a_html=(li_html[i].find('a'))
    title=a_html.text.strip()
    link=a_html['href']
    insert_row(title,link)
client.commit()