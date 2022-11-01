from random import random,choice
from statistics import median
import time
import msvcrt

def createMap(w, h):
    return [[1] * w for i in range(h)]

def clear(m,x,y):
    if x in range(len(m[0])) and y in range(len(m)):
        m[y][x] = 0

def generateLevel(m, n):
    c_x = len(m[0])//2
    c_y = len(m)//2
    direction = choice([0,1,2,3])
    clear(m,c_x,c_y)
    
    while n > 0:
        if direction == 0:
            if median([2,len(m)-3,c_y]) == c_y:
               c_y -= 1
        if direction == 1:
            if median([2,len(m[0])-3,c_x]) == c_x:
               c_x += 1
        if direction == 2:
            if median([2,len(m)-3,c_y]) == c_y:
               c_y += 1
        if direction == 3:
            if median([2,len(m[0])-3,c_x]) == c_x:
               c_x -= 1
        if m[c_x][c_y]:
            clear(m,c_x,c_y)
            direction = choice([0,1,2,3])
            n -= 1
        else:
            direction = choice([0,1,2,3])



def createPlayer():
    pass

def getInput():
    key = msvcrt.getch()
    print(chr(key))

def movePlayer():
    pass

def displayMap(m):
    for i in m:
        for k in i:
            if k:
                print("[]",end="")
            else:
                print("  ",end="")
        print("")

def main():
    world = createMap(20,20)
    generateLevel(world, 80)
    createPlayer()
    while (True):
        #getInput()
        movePlayer()
        displayMap(world)
        #time.sleep(0.05)
        break;

if __name__ == '__main__':
    main()