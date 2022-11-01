from graphics import *
from random import randint
from math import sqrt

scr_w,scr_h = 1024,1024
win = GraphWin("Langton's Ant", scr_w, scr_h, autoflush=False)

class Ball:
    def __init__(self,pos,radius,win):
        self.locked = False
        self.pos = pos
        self.prevPos = pos
        #self.vel = [0,9.8]
        self.radius = radius
        self.win = win
        self.body = Circle(Point(self.pos[0],self.pos[1]),self.radius)
        self.body.draw(self.win)
        self.body.setFill(color_rgb(randint(0,255),randint(0,255),randint(0,255)))

    def update(self):
        if not self.locked:
            posBeforeUpdate = self.pos
            self.pos += [self.pos[0] - self.prevPos[0], self.pos[1] - self.prevPos[1]]
            self.pos += [self.pos[0], self.pos[1] + 9.8]
            self.prevPos = posBeforeUpdate
            self.body.move(self.pos[0] - self.prevPos[0], self.pos[1] - self.prevPos[1])

    def wasClicked(self,mp):
        return sqrt((self.pos[0] - mp.getX())**2 + (self.pos[1] - mp.getY())**2) <= self.radius


class Link:
    def __init__(self, Ball1, Ball2, length,win):
        self.Ball1 = Ball1
        self.Ball2 = Ball2
        self.length = length
        self.body = Line(self.Ball1.body.getCenter(),self.Ball2.body.getCenter())
        self.win = win
        self.body.draw(self.win)

    def update(self):
        stickCenter = [(self.Ball1.pos[0] + self.Ball2.pos[0]) / 2, (self.Ball1.pos[1] + self.Ball2.pos[1]) / 2]
        stickDir = Vnormalize([(self.Ball1.pos[0] - self.Ball2.pos[0]), (self.Ball1.pos[1] - self.Ball2.pos[1])])
        if not self.Ball1.locked:
            self.Ball1.pos = [(stickCenter[0] + stickDir[0]) * self.length / 2, (stickCenter[1] + stickDir[1]) * self.length / 2]     
        if not self.Ball2.locked:
            self.Ball2.pos = [(stickCenter[0] - stickDir[0]) * self.length / 2, (stickCenter[1] - stickDir[1]) * self.length / 2]      

def Vnormalize(v):
    return [v[0]/sqrt(v[0]**2 + v[1]**2),v[1]/sqrt(v[0]**2 + v[1]**2)]

def main():
    balls = []
    sticks = []
    while True:
        mouseInput = win.checkMouse()
        if mouseInput != None:
            for b in balls:
                if b.wasClicked(mouseInput):
                    b.locked = not b.locked
                    break
            else:
                k = Ball([mouseInput.getX(),mouseInput.getY()],25,win)
                k.locked = True
                c = Ball([mouseInput.getX()+100,mouseInput.getY()],25,win)
                s = Link(k,c,100,win)
                sticks += [s]
                balls += [k,c]

        for b in balls:
            b.update()

        for s in sticks:
            s.update()

        inp = win.checkKey()
        if inp != "":
            if inp == "q":
                win.close()
                break
        update(10)

if __name__ == '__main__':
    main()