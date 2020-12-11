import random
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
