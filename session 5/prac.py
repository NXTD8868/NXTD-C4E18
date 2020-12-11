td={
    'lmao':'laugh my a off',
    'lol':'laugh out loud',
    'ng' : 'nguoi'
}
off=0
while off!=1:
    for key in td:
        print(f'{key}',end='\t')
    print('')
    ui=input('your code: ')
    if ui in td:
        print(td[ui])
    else:
        ask=input('do you want to add this word Y/N: ')
        ask=ask.lower()
        if ask=='y':
            add = input('def: ')
            td[ui]=add
        elif ask=='n':
            off=1