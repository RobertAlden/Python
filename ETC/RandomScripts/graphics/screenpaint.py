import graphics as g

scr_w = 480
scr_h = 480

def main():
    win = g.GraphWin("Pretty Colors", scr_w, scr_h)
    win.setBackground("black")

    for i in range(scr_w):
        for k in range(scr_h):
            g.plot(i, k, g.color_rgb(i % 255, k % 255, i * k % 255))





if __name__ == '__main__':
    main()