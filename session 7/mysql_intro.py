import pymysql
client=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Thaiduong8868'
)

board=client.cursor() 
# tao ra querry o workbench
def create_database():
    board.execute('CREATE DATABASE `from_python`')

#thuc hien lenh tren work bench day
def create_board():
    board.execute('''CREATE TABLE `from_python`.`pytable1`(
        customer varchar(255),
        product varchar(255),
        phone varchar(255),
        price decimal(19,2),
        quantity int(11)
    )''')        
# mo ngoac bang 3 dau ''' neu xuong dong
def insert_row():
    board.execute('''
    INSERT INTO `from_python`.`pytable1`(
        customer,
        product,
        phone,
        price,
        quantity
    ) VALUES (
        'KH12',
        'sp123',
        '093848475',
        78900,
        9
    
    )''')
insert_row()
client.commit()