from math import sqrt, cos, sin, atan2
from graphics import *


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def p2c_x(length, direction):
    return length * cos(direction)


def p2c_y(length, direction):
    return length * sin(direction)


def c2p_angle(x0, y0, x1, y1):
    return atan2(y1 - y0, x1 - x0)


def point_distance(x0, y0, x1, y1):
    return sqrt((x1 - x0)**2 + (y1 - y0)**2)



