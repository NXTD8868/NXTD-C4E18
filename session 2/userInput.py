import math
a = input('nhap ten : ')
dc = input('dia chi: ')
print(type(a))
t=int(input('nam sinh: '))
print(a,' ',dc,' ',2020-t)


weight=float(input('can nang: '))
height=float(input('chieu cao: '))
print('Chi so BMI la: ',weight/(height**2))
radius=float(input('ban kinh hinh tron: '))
print('chu vi hinh tron la: ',"{:.2f}".format(radius*2*math.pi),' dien tich hinh tron la: ',"{:.2f}".format((radius**2)*math.pi))