from random import random,choice

size = 21

world = []
for i in range(size):
    r = [1] * size
    world.append(r)

def display():
    for i in world:
        for k in i:
            if k:
                print("[]",end="")
            else:
                print("  ",end="")
        print("")

def clear(x,y):
    if x in range(size) and y in range(size):
        world[y][x] = 0
def fill(x,y):
    if x in range(size) and y in range(size):
        world[y][x] = 1

def room(x,y,w,h):
    for k in range(y,y+h):
        for i in range(x,x+w):
            clear(i,k)

def random_walker(n):
    c_x = size//2
    c_y = size//2
    direction = choice([0,1,2,3])
    clear(c_x,c_y)
    
    while n > 0:
        if direction == 0:
            c_y -= 1
        if direction == 1:
            c_x += 1
        if direction == 2:
            c_y += 1
        if direction == 3:
            c_y -= 1
        
        clear(c_x,c_y)
        direction = choice([0,1,2,3])


random_walker(20)

display()