from turtle import*
import random
#1
color=['red','blue','brown','yellow','grey']
for i in range (3,8):
    pencolor(color[i-3])
    for n in range(i):
        forward(100)
        right(180-(180*(i-2)/i))

mainloop()
#2
flock=[43,412,212,80,32,56,350]
total=0
n = int(input('month: '))
for i in range(n):
    for i in range(len(flock)):
        flock[i]=flock[i]+50
    print('one month has passed, now heres the flock: ')
    print(flock)
    max=flock[0]
    for x in range(len(flock)):
        if max<=flock[x]:
            max=flock[x]
    print('now my biggest sheep has the size ',max,' lets sheer it')
    flock[flock.index(max)]=8
    print('after sheering heres my flock: ')
    print(flock)
for g in range(len(flock)):
    total = total +flock[g]
print('my total flock size: ',total)
print('I would get ',total,' * 2$ = ',total*2,'$')

#3

stuff=['lmao','sheep','cat','yolo']
while len(stuff)!=0:
    ca=stuff[random.randint(0,len(stuff)-1)]
    puz=list(ca)
    random.shuffle(puz)
    print(puz)
    full=''
    for i in ca:
        full=full+i
    ans=input('dap an: ')
    if ans==full:
        stuff.remove(full)
    elif ans!=full:
        print(':(')
    
