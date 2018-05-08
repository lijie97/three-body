#Name: Three body problem
#Language : Python 3
from turtle import *
from random import randint
from time import sleep
sgn = lambda x:1 if x>=0 else -1

class star:
    listOfStars=[]
    k=1
    def __init__(self, pos, mass, velocity,name,color):
        self.x,self.y=pos
        self.mass=mass
        self.v_x,self.v_y=velocity
        star.listOfStars.append(self)
        self.name=name
        self.color=color
    def change_pos(self):
        self.x+=self.v_x/10
        self.y+=self.v_y/10
    def change_vel(self):
        self.v_x+=self.a_x
        self.v_y+=self.a_y
    def get_acce(self):
        self.a_x=0
        self.a_y=0
        for i in star.listOfStars:
            if id(i)!=id(self):
                d = ((self.x-i.x)**2+(self.y-i.y)**2)**1/2
                self.a_x+=(i.x-self.x)*i.mass/d
                self.a_y+=(i.y-self.y)*i.mass/d
    def output(self):
        up()
        goto(int(self.x)/30,int(self.y)/30)
        down()
        dot((int(self.mass**0.3))+2,self.color)
        up()
    def outputG(self):
        up()
        goto(int(self.x)/30,int(self.y)/30)
        down()
        dot((int(self.mass**0.3))+10,self.color)
        up()
    def setK(k):
        star.k=k
screensize(canvwidth=None, canvheight=None, bg="white")
#sleep(6)
write("Étoile double+planète grande")
#p1=(1187, -150)
#v1=(-15, 43)
#p2=(1918, 797)
#v2=(87, 12)
#p3=(-1598, 524)
#v3=(-7, -63)
p1=(8000, 0)
p2=(-8000, 0)
v1=(0,31.5)
v2=(0,-31.5)
star.listOfStars=[]
sun=star(p1,100,v1,"sun","red")
sun2=star(p2,100,v2,"sun2","orange")
earth=star((6000,0),100,(0,0),"earth","blue")
#sun3=star(p3,100,v3,"sun3","orange")
hideturtle()
speed(0)
for i in star.listOfStars:
    i.outputG()
    write("t="+str(0))
#for i in star.listOfStars:
#    print(i.x,i.y)
#star.setK(2)
t=0
tracer(10000)
while True:
    #if not t%100:print(t)
    t+=1
    #print(earth.v_x,earth.v_y)
    for i in star.listOfStars:
        i.get_acce()
    for i in star.listOfStars:
        i.change_vel()
    for i in star.listOfStars:
        i.change_pos()
    for i in star.listOfStars:
        i.output()
        
    bln=False
    if not t%7900:
        clear()
        for i in star.listOfStars:
            i.outputG()
            write("t="+str(t))
        home()
        write("Étoile double+planète grande")
