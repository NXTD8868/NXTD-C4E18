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
print(list)
