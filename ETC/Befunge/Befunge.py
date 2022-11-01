import sys
import os.path
import re
import getch
import time

filename = sys.argv[1]
if not os.path.isfile(filename):
    print('File does not exist.')
else:
    data = []
    with open(filename) as f:
        for l in f:
            data += [l]
    width = len(data[0])
    height = len(data)
    print(width,height)
    data = "".join(data)
    field = []
    for h in range(height):
        row = [0]* width
        field.append(row)

    for i in range(len(data)):
        x = i % width
        y = int(i / width)
        field[y][x] = str(data[i])

    def disp():
        for i in field:
            print(i)

    disp()

    