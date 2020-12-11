key = 0
list=['T-shirt','Hoodie']
while key==0:
    print('welcome to our shop,what do you want? (C R U D): ')
    print('to exit the shop enter "EXIT" ')
    user_input=input('input:... ')
    if user_input=='EXIT':
        key=1
        break
    else:
        user_input=user_input.lower()
        if user_input=='c':
            a=input('add?:  ')
            list.append(a)
            print('our updated list:')
            for i in range(len(list)):
                print(f'{i+1}.{list[i]}')
        elif user_input=='r':
            print('out list: ')
            for i in range(len(list)):
                print(f'{i+1}.{list[i]}')
        elif user_input == 'u':
            a=int(input('position you want to update: '))
            if a>=len(list)+1:
                print('invalid')
            else:
                b=input('enter new item: ')
                list[a-1]=b
                print('our updated list: ')
                for i in range(len(list)):
                    print(f'{i+1}.{list[i]}')
        elif user_input== 'd':
            a=int(input('position you want to delete: '))
            if a>=len(list)+1:
                print('invalid')
            else:
                list.pop(a-1)
                print('out updated list: ')
                for i in range(len(list)):
                    print(f'{i+1}.{list[i]}')

    
    

