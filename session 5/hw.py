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
