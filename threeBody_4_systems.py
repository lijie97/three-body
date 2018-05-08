#Name: Three body problem
#Language : Python 3
from turtle import *
from random import randint
from time import sleep
sgn = lambda x:1 if x>=0 else -1

class star:
    k=1
    def __init__(self, pos, mass, velocity,name,color,groupOfStar):
        self.x,self.y=pos
        self.mass=mass
        self.v_x,self.v_y=velocity
        self.name=name
        self.color=color
        self.groupOfStar=groupOfStar
    def change_pos(self):
        self.x+=self.v_x/10
        self.y+=self.v_y/10
    def change_vel(self):
        self.v_x+=self.a_x
        self.v_y+=self.a_y
    def get_acce(self):
        self.a_x=0
        self.a_y=0
        for i in self.groupOfStar:
            if id(i)!=id(self):
                d = ((self.x-i.x)**2+(self.y-i.y)**2)**1/2
                self.a_x+=(i.x-self.x)*i.mass/d
                self.a_y+=(i.y-self.y)*i.mass/d
    def output(self,x0,y0):
        up()
        goto(int(self.x)/40+x0,int(self.y)/40+y0)
        down()
        dot((int(self.mass**0.3))+2,self.color)
        up()
    def outputG(self,x0,y0):
        up()
        goto(int(self.x)/40+x0,int(self.y)/40+y0)
        down()
        dot((int(self.mass**0.3))+10,self.color)
        up()
    def setK(k):
        star.k=k
    def __str__(self):
        return(self.name+":\n"+"    Velocity:\n       "+str((self.v_x,self.v_y))+"\n    Pos:\n        "+str((self.x,self.y))+"\n    Groupe:"+str(self.groupOfStar))
        


class groupOfStars(list):
    def setName(self,name):
        self.name=name
    def setCentre(self,x0,y0):
        self.x0,self.y0=x0,y0
    def frame(self):
        #for i in self:
        #    print(i)
        #input()
        for i in self:
            i.get_acce()
        for i in self:
            i.change_vel()
        for i in self:
            i.change_pos()
        for i in self:
            i.output(self.x0,self.y0)
        bln=False
        if not t%7900:
            for i in self:
                i.outputG(self.x0,self.y0)
                write("t="+str(t))
            up()
            goto(self.x0,self.y0)
            down()
            write(self.name)

def table():
    home()
    down()
    goto(1000,0)
    home()
    goto(-1000,0)
    home()
    goto(0,1000)
    home()
    goto(0,-1000)
    up()
    
screensize(canvwidth=1920, canvheight=1080, bg="white")
setup(width=0.99, height=0.99, startx=None, starty=None)
up()
hideturtle()
speed(0)
table()
tracer(20000)

p1=(8000, 0)
p2=(-8000, 0)
v1=(0,31.5)
v2=(0,-31.5)

g1=groupOfStars()
g1.extend([star(p1,100,v1,"sun","red",g1),star(p2,100,v2,"sun2","orange",g1),star((6000,0),100,(0,0),"earth","blue",g1)])
g1.setName("Étoile double+planète grande")
g1.setCentre(500,-300)

goto(g1.x0,g1.y0)
write(g1.name)
#
for i in g1:
    i.outputG(g1.x0,g1.y0)
    up()
    goto(g1.x0,g1.y0)
    write("t="+str(0))
#input()
g2=groupOfStars()
g2.extend([star(p1,100,v1,"sun","red",g2),star(p2,100,v2,"sun2","orange",g2)])
g2.setName("Étoile double")
g2.setCentre(-500,300)

goto(g2.x0,g2.y0)
write(g2.name)

for i in g2:
    i.outputG(g2.x0,g2.y0)
    up()
    goto(g2.x0,g2.y0)
    write("t="+str(0))
#for i in star.listOfStars:
#    print(i.x,i.y)
#star.setK(2)

g3=groupOfStars()
g3.extend([star(p1,100,v1,"sun","red",g3),star(p2,100,v2,"sun2","orange",g3),star((6000,0),0.001,(0,0),"earth","blue",g3)])
g3.setName("Étoile double+planète petite")
g3.setCentre(500,300)

goto(g3.x0,g3.y0)
write(g3.name)

for i in g3:
    i.outputG(g3.x0,g3.y0)
    up()
    goto(g3.x0,g3.y0)
    write("t="+str(0))

g4=groupOfStars()
g4.extend([star(p1,100,v1,"sun","red",g4),star(p2,100,v2,"sun2","orange",g4),star((6000,0),10,(0,0),"earth","blue",g4)])
g4.setName("Étoile double+planète moyenne")
g4.setCentre(-500,-300)

goto(g4.x0,g4.y0)
write(g4.name)

for i in g4:
    i.outputG(g4.x0,g4.y0)
    up()
    goto(g4.x0,g4.y0)
    write("t="+str(0))
    
t=0


while True:
    if not t%7900:
        clear()
        table()
    g1.frame()
    g2.frame()
    g3.frame()
    g4.frame()
    t+=1
        
    
