from graphics import *
import multiprocessing as mp


def point(xy):
    global win
    win.plot(xy[0],xy[1],color_rgb(xy[0]%255,xy[1]%255,(xy[0]+xy[1])%255))

if __name__ == '__main__': 
    scr_width,scr_height = 256,256
    win = GraphWin("Dungeon Crawler", scr_width,scr_height)
    win.setBackground("white")

    points = [(i,k) for i in range(scr_width) for k in range(scr_height)]

    with mp.Pool() as p:
        results = p.map(point,points)
    win.getMouse()
    win.close()