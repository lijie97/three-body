#Name: Three body problem
#Language : Python 3
from turtle import *
from random import randint

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
                self.a_x+=(i.x-self.x-self.x)*i.mass/d
                self.a_y+=(i.y-self.y)*i.mass/d
    def output(self):
        up()
        goto(int(self.x)/10,int(self.y)/10)
        down()
        dot((int(self.mass**0.3))+1,self.color)
        up()
    def setK(k):
        star.k=k
screensize(canvwidth=None, canvheight=None, bg="black")
while True:
    p1=(randint(-2000,2000),randint(-2000,2000))
    v1=(randint(-100,100),randint(-100,100))
    p2=(randint(-2000,2000),randint(-2000,2000))
    v2=(randint(-100,100),randint(-100,100))
    p3=(randint(-2000,2000),randint(-2000,2000))
    v3=(randint(-100,100),randint(-100,100))
    star.listOfStars=[]
    sun=star(p1,100,v1,"sun","red")
    sun2=star(p2,100,v2,"sun2","white")
    #earth=star((2000,2000),1,(-80,80),"earth","blue")
    sun3=star(p3,100,v3,"sun3","orange")
    hideturtle()
    speed(0)
    #for i in star.listOfStars:
    #        i.output()
    #for i in star.listOfStars:
    #    print(i.x,i.y)
    #star.setK(2)
    t=0
    tracer(10+t/100)
    while True:
        #print(p1,p2,p3)
        t+=1
        for i in star.listOfStars:
            i.get_acce()
        #print(sun.a_x,sun.a_y)
        for i in star.listOfStars:
            i.change_vel()
        #print(sun.v_x,sun.v_y)
        for i in star.listOfStars:
            i.change_pos()
        
        #print(sun.x,sun.y)
        #for i in star.listOfStars:
        #    i.output()
        if t==30000:
            print(p1,v1)
            print(p2,v2)
            print(p3,v3)
            break
        bln=False
        #print(i.x,i.y)
        for i in star.listOfStars:
            #print(not(-60000<=i.x<=60000))
            #print(not(-60000<=i.y<=60000))
            #print((not(-60000<=i.x<=60000)) or (not(-60000<=i.y<=60000)))
            if (not(-60000<=i.x<=60000)) or (not(-60000<=i.y<=60000)):
                bln=True
                #print(1)
                #print(i.x,i.y)
                break
        if bln:
            #print(1)
            break
            
