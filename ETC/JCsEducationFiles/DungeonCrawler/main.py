from graphics import *
from random import randint, choice, random
from statistics import median
from math import sqrt


# This section is largely boiler-plate stuff for making a grid based world.
# The only parts that should be adjusted are scr_width and scr_height for the size of the window,
# (Keep them equal btw, pretty sure it doesn't works with non-square tiles at the moment)
# And cell_count, which will affect how many cell tall and across are fit into the window
# Making it bigger will make all the cells smaller, and try to keep it a power of two in size
scr_width,scr_height = 1024,1024
win = GraphWin("Dungeon Crawler", scr_width,scr_height)
win.setBackground("white")
cell_count = 64
c_width = scr_width//cell_count
c_height = scr_height//cell_count


# Just a wrapper function for the graphic library's rectangle function
def makeRects(x,y,w,h):
    return Rectangle(Point(x*w,y*h),Point(x*w+w,y*h+h))

# More boiler-plate, sets up a 2D array full of rectangles, and then a second one of 1's and 0's to control
# what rectangles are visible
display_grid = [[makeRects(i,k,c_width,c_height) for k in range(cell_count)] for i in range(cell_count)]
world = [[1 for i in range(cell_count)] for k in range(cell_count)]
for r,row in enumerate(world):
    for c,val in enumerate(row):
        display_grid[r][c].setFill("black")

player = Circle(Point(cell_count//2 * c_width + c_width/2,cell_count//2 * c_height + c_height/2),c_width/2)
player.setFill("green")

exit = Circle(Point(c_width/2,c_height/2),c_width/2)
exit.setFill("yellow")

gen_level = True
level = 1

# Removes the headache of making sure we stay within the bounds of the map when
# clearing spaces for the new level, as well as verifying we have removed a wall when
# we try to clear a space. If it returns false, it means that the space was already cleared
def clear(x,y):
    if x in range(cell_count) and y in range(cell_count):
        if world[x][y]:
            world[x][y] = 0
            return True
    return False

# Applies a movement in a given direction to an x,y position and returns the new position
def move(x,y,direct):
    if direct == "UP":
        y -= 1
    if direct == "RIGHT":
        x += 1
    if direct == "LEFT":
        y += 1
    if direct == "DOWN":
        x -= 1
    x = median([1,cell_count-2,x])
    y = median([1,cell_count-2,y])
    return (x,y)

# Simplest level generation, involves a random walker algorithm that makes cavelike mazes,
# levels should have approximately n empty squares.
def generate_level_type1(n):
    #Start at the center of the map, clearing the space and pick a direction
    c_x = cell_count//2
    c_y = cell_count//2
    direction = choice(["UP","RIGHT","DOWN","LEFT"])
    world[c_x][c_y] = 0
    n -= 1
    attempts = 0
    # While we still have squares left to empty
    while n > 0:
        c_x,c_y = move(c_x,c_y,direction) # Move in a direction
        if clear(c_x,c_y): # If the space was a wall, make it empty
            direction = choice(["UP","RIGHT","DOWN","LEFT"]) # New direction
            n -= 1
            attempts = 0 # Reset attempts counter
        else: # Otherwise if we failed to clear a new spot
            attempts += 1 
            if attempts > 5: # if we fail 5 times in a row pick a new direction, and roll to see if we return to center
                attempts = 0
                if random() < .1:
                    c_x = cell_count//2
                    c_y = cell_count//2
                direction = choice(["UP","RIGHT","DOWN","LEFT"])

# Intermediate level generation, involves a random walker algorithm that makes hallways
def generate_level_type2(n):
    c_x = cell_count//2
    c_y = cell_count//2
    direction = choice(["UP","RIGHT","DOWN","LEFT"])
    world[c_x][c_y] = 0
    n -= 1
    dist = randint(1,2) * 3 # This variable is the main difference between this version and the last
                            # It controls the length of a given hallway
    attempts = 0
    while n > 0:
        while dist > 0: # while the hallway is still being built keep clearing out spaces
            dist -= 1
            c_x,c_y = move(c_x,c_y,direction)
            if clear(c_x,c_y):
                n -= 1
                attempts = 0
            else:
                attempts += 1
                if attempts > 5: # If we fail 5 times in a row, end the current hallway, and start a new one,
                                 # potentially at the center of the map
                    attempts = 0
                    dist = 0
                    if random() < .1:
                        c_x = cell_count//2
                        c_y = cell_count//2
        direction = choice(["UP","RIGHT","DOWN","LEFT"])
        dist = randint(1,2) * 2 # Start a new hallway

# Advanced level generation, involves a random walker algorithm that makes hallways AND occasionally places rooms
def generate_level_type3(n): # This is largely identical to the last one
    c_x = cell_count//2
    c_y = cell_count//2
    direction = choice(["UP","RIGHT","DOWN","LEFT"])
    world[c_x][c_y] = 0
    n -= 1
    max_dist = 10
    dist = randint(2,5) * 2
    attempts = 0
    while n > 0:
        while dist > 0:
            dist -= 1
            c_x,c_y = move(c_x,c_y,direction)
            if clear(c_x,c_y):
                n -= 1
                attempts = 0
            else:
                attempts += 1
                if attempts > dist:
                    attempts = 0
                    if random() < .1:
                        c_x = cell_count//2
                        c_y = cell_count//2
        if random() < .1: # until here, where we have a 1:10 chance to create a room between 3-6 tiles wide and tall
            width = randint(3,6)
            height = randint(3,6)
            n -= makeRoom(c_x-width//2,c_y-height//2,width,height)
        direction = choice(["UP","RIGHT","DOWN","LEFT"])
        dist = randint(1,2) * 2

# Used in generate_level_type3 to make a room starting with the x,y of the
# top left corner, plus the width and height
def makeRoom(x,y,w,h):
    n = 0
    for i in range(w):
        for k in range(h):
            if clear(x+i,y+k):
                n += 1
    return n

# Initalizes the graphics objects for the map and the player/exit
# Probably dont mess with this one
def display(): 
    for r,row in enumerate(world):
        for c,val in enumerate(row):
            display_grid[r][c].undraw()    
            if val:
                display_grid[r][c].draw(win)
    player.undraw()
    player.draw(win)
    exit.undraw()
    exit.draw(win)

# Turns keyboard presses into movement.
def handle_input():
    global gen_level
    global level

    k_inp = win.getKey() # Gets the string associated with the key pressed
    px,py = int(player.getCenter().getX()//c_width),int(player.getCenter().getY()//c_height)
    ex,ey = int(exit.getCenter().getX()//c_width),int(exit.getCenter().getY()//c_height)
    npx,npy = px,py # creating a copy of the players position to check for wall collisions
    if k_inp == "w":
        npy -= 1
    if k_inp == "s":
        npy += 1
    if k_inp == "a":
        npx -= 1
    if k_inp == "d":
        npx += 1

    if not world[npx][npy]: # if no wall is present, move there
        player.move((npx-px)*c_width,(npy-py)*c_height)

    if npx == ex and npy == ey: # if the player reaches the exit go to next level
        gen_level = True
        level+=1
        move_to_center(player)
        exit.move(-exit.getCenter().getX(),-exit.getCenter().getY())
        exit.move(c_width//2,c_height//2)

    if k_inp == "q": # if you hit q, it closes the game
        win.close()
        quit()

def distance_from_player(xy): 
    return sqrt((xy[0] - cell_count//2)**2 + (xy[1] - cell_count//2)**2)

def move_to_center(k):
    x,y = k.getCenter().getX() - scr_width//2 + c_width//2 , k.getCenter().getY() - scr_height//2 + c_height//2
    k.move(-x,-y)

def main():
    while True: # Main game loop
        global gen_level
        global world

        if gen_level:
            world = [[1 for i in range(cell_count)] for k in range(cell_count)]
            level_type = choice([1,2,3]) # Picks a random algorithm to generate the next floor
            level_size = level * 50
            if level_type == 1:
                generate_level_type1(level_size)
            if level_type == 2:
                generate_level_type2(level_size)
            if level_type == 3:
                generate_level_type3(level_size) 
            gen_level = False 
            z = 0
            spaces = []
            for r,row in enumerate(world): # finds all empty spaces
                for c,val in enumerate(row):
                    if not val:
                        z += 1
                        spaces.append((r,c)) 
            spaces.sort(key=distance_from_player,reverse=True) # moves the exit to the one furthest from the center of the map, where the player always spawns
            exit.move(spaces[0][0]*c_width,spaces[0][1]*c_height)
            display()
            player.undraw()
            player.draw(win)
            exit.undraw()
            exit.draw(win)
        handle_input()


if __name__ == '__main__':
    main()
