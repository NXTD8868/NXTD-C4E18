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