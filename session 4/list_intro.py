list = ['com','rau','trung','thit','canh'] #container data type
print(list)
#C R U D
#Create

list.append('ca')
print(list)
#Read
print(list[3])
print(len(list))
for i in range(len(list)):
    print(f'{i}.{list[i]}')
#Update
list[3]='sua'
print(list)
#Delete
list.remove('canh')
print(list)
list.pop(2)
delete_item=list.pop(0)#delete by index, then assign to a var
print(list)

#find index by value
print(list.index('rau'))
#check if a value exist or not (return boolean)
print('rau' in list)
print('lmao' in list)
user_input=input('nhap :')
if user_input in list:
    print(list.index(user_input))