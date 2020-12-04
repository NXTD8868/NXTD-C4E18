import math
weight=float(input('can nang: '))
height=float(input('chieu cao: '))
BMI= (weight/(height**2))
if BMI<18.5:
    print('underweight')
elif BMI>=18.5 and BMI<24.9:
    print('normal weight')
else:
    print('overweight')

a=int(input('nhap a: '))
b=int(input('nhap b: '))
c=int(input('nhap c: '))
delta = b**2-(4*a*c)

if delta<0:
    print('pt vo no')
elif delta==0:
    print('pt co 1 no: ',(0-b)/(2*a))
else:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print('pt co 2 no: ',x1,' va ',x2)