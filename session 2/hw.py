#condition
#1. Nhập vào 1 năm, kiểm tra xem năm đó phải năm đó có bao nhiêu ngày?
 
i=int(input('nhap nam: '))
if i%100==0:
    if(i%400==0):
        print(i,' co 366 ngay')
    else:
        print(i,' co 365 ngay')
elif i%100!=0:
    if i%4==0:
        print(i,' co 366 ngay')
    else:
        print(i,' co 365 ngay')

#2. Nhập vào 1 tháng trong năm, in ra màn hình số ngày của tháng đó (Yêu cầu kiểm tra cả năm nhuận).

k=0
i=int(input('nhap nam: '))
t=int(input('nhap thang: '))
if i%100==0:
    if(i%400==0):
        k=1
    else:
        k=0
elif i%100!=0:
    if i%4==0:
        k=1
    else:
        k=0
if t==1 or t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12:
    print(t,' co 31 ngay')
else:
    if t!=2:
        print(t,' co 30 ngay')
    else:
        if k == 1:
            print(t,' co 29 ngay')
        else: 
            print(t, ' co 28 ngay')
#3. Nhập vào 1 tháng trong năm, in ra mùa của tháng đó
t = int(input('nhap thang: '))
if t<=3:
    print('mua dong')
elif t>=4 and t<=6:
    print('mua xuan')
elif t>=7 and t<=9:
    print('mua ha')
else:
    print('mua dong')
#4. Nhập vào 3 số a, b, c. In ra theo thứ tự tăng dần.
a=int(input('nhap a: '))
b=int(input('nhap b: '))
c=int(input('nhap c: '))
if a<= b and a<=c:
    if b<c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b<= b and b<=c:
    if a<c:
        print(b,a,c)
    else:
        print(b,c,a)
elif c<=b and c<=a:
    if b<a:
        print(c,b,a)
    else:
        print(c,a,b)
#5. Nhập vào 3 số a, b, c. Kiểm tra xem 3 số đó có lập được thành tam giác không. Nếu có, kiểm tra xem tam giác có vuông, cân hay đều k?
a=int(input('nhap a: '))
b=int(input('nhap b: '))
c=int(input('nhap c: '))
if a+b>c and b+c>a and c+a>b:
    if a==b or b==c or c==a:
        print('abc la tam giac can')
    elif a==b==c:
        print('abc la tam giac deu')
    else:
        print('abc la tam giac')
else:
    print('abc ko phai la tam giac')

#loop
#1 Thực hiện tính tổng: S = 1 + 2 + 3 + … + N với N nhập từ bàn phím
n = int(input('nhap n: '))
i = len(range(1,n+1))
print(i)
s=((1+n)/2)*i
print(s)
#2. Thực hiện tính tổng: S = 1 + 3 + 5 + … + 2N + 1 với N nhập từ bàn phím.
n = int(input('nhap n: '))
s=0
for i in range(1,2*n+2,2):
    s=s+i

print(s)

#3. Thực hiện tính tổng: S = 2 + 4 + 6 + … + 2N với N nhập từ bàn phím.
n = int(input('nhap n: '))
s=0
for i in range(1,2*n+1,1):
    if i%2==0:
        s=s+i

print(s)

#4. Thực hiện tính tổng: S = 1/1 +1/2+1/3+...+1/n với N nhập từ bàn phím
n = int(input('nhap n: '))
s=0
for i in range(1,n+1):
    s=s+1/i
print(s)
#5
n = int(input('nhap n: '))
s=0
for i in range(1,n+1):
    s=s+1/((i+1)*i)
print(s)
#6 fibonacci

n = int(input('nhap n: '))
a=1
b=1
s=2
for i in range(n-1):
    c=a+b
    s=s+c
    a=b
    b=c
print(a)
print(s-c)
#7
a=int(input('nhap chieu dai '))
b=int(input('nhap chieu rong '))
for i in range(b):
    for k in range(a):
        print('*',end='')
    print('')
#8
a=int(input('nhap chieu dai '))
for i in range(a):
    for k in range(i):
        print('*',end='')
    print('')

