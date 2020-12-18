from turtle import*
def draw_square(l):
    for i in range(4):
        forward(l)
        right(90)


#turtle 1
n = int(input('nhap n:'))
speed(100000)
for i in range(n):
    draw_square(70)
    right(360/n)
#turtle 2
a=200
for i in range(n):
    draw_square(a)
    right(360/n)
    a=a-a/n

mainloop()
#standardise name
s = input('enter yout full name: ')
j= s.split(' ')
for i in range(len(j)):
    j[i]=j[i].lower()
    j[i]=j[i].title()
final=''
for i in range(len(j)):
    final=final+j[i]
    if i == len(j)-1:
        break
    final=final+' '
print('updated: ',final)
    
print(final)
#bank statement
acc= input('enter your balance: ')
acc=list(acc)
print(acc)
eli=0
for i in range(len(acc)):
    if acc[i]=='0':
        eli+=1
    elif acc[i]!='0':
        break
print(eli)
for i in range(eli):
    acc.pop(0)
acc.reverse()
print(acc)
new=[]
for i in range(len(acc)):
    new.append(acc[i])
    if (i+1)%3==0:
        new.append(',')
print(new)
if new[-1]==',':
    new.pop(-1)
new.reverse()
final=''
for i in range(len(new)):
    final+=new[i]
print('your updated balance: $',final)
#inventory
inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket']=['seashell','strange berry','lint']
print(inventory)
inventory['backpack'].remove('dagger')
print(inventory)
inventory['gold']+=50
print(inventory)
#count occurence
#without count()
oc=0
my_list=[1,2,3,4,5,3,12,312,54,345,1,1,1,1,1,1,1,1,1,1]
s=int(input('enter a number: '))
for i in range(len(my_list)):
    if my_list[i]==s:
        oc+=1
print('the number ',s,'appears',oc,' times in the list')

#with count()
result=my_list.count(s)
print('the number ',s,'appears',result,' times in the list')
#stock and price
total=0
prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key in prices:
    total=total+prices[key]*stock[key]
    print(key)
    print('prices: ',prices[key])
    print('stock: ',stock[key])
    print()
print(total)