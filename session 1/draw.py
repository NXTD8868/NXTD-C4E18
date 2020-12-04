from turtle import *
import random
for x in range(360):             #draw circle 
    right(1)                     #circle(radius)  actual func 
    forward(1)
                                #pen up leave no line

for x in range(3): 
    forward(100)                #triangle
    right(120)              


for x in range(4):
    forward(100)            #square
    right(90)


for x in range(6):
    forward(100)
    right(60)           #hexagon
for i in range(3):
    x = random.randint(0,30)
    y = random.randint(0,30)
    r = random.randint(50,150)#circle
    setpos(x,y)
    circle(r)

for i in range(15):
    forward(100)
    left(145)            #star
    forward(100)
    left(145)
# forward(100)
mainloop()