a= range(9,1,-1)
print(*a)
for i in range(9):
    print(i)

#1
for i in range(0,101):
    print(i)
#2
for i in range(100,-1,-1):
    print(i)
#3
for i in range(0,100,2):
    print(i)
for i in range(1,101,2):
    print(i)
#4
n = int(input('nhap n: '))
i = len(range(1,n+1))
print(i)
s=((1+n)/2)*i
print(s)
#5
n = int(input('nhap n: '))
s=0
for i in range(1,2*n+2,2):
    s=s+i

print(s)

#6
n = int(input('nhap n: '))
s=0
for i in range(1,2*n+1,1):
    if i%2==0:
        s=s+i

print(s)
