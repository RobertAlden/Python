#!/usr/bin/env python3

import sys
import os.path
import re
import getch
import time
import colorama

bf = re.compile('[\+\-\]\[\<\>\.\,]+')
# Define a filename.
filename = sys.argv[1]
verbose = False
if len(sys.argv) > 2:
    speed = float(sys.argv[2])
    verbose = True
else:
    speed = 0
if not os.path.isfile(filename):
    data = filename
    #print('File does not exist.')
else:
    with open(filename) as f:
        data = "".join(f.readlines())

memory = [0] * 30000
traversed = [False] * 30000
index = 0
inst = 0
loopstack = []
data = "".join(data.split("\n"))
data = bf.findall(data)
data = "".join(data)
output = ""

size = len(data)
try:
    while inst < size:
        traversed[index] = True
        if verbose:
            if speed != 0:
                time.sleep(speed)
            print(str(inst)+":"+data[inst] + " " + " ".join([str(m) if ind != index else "`"+str(m) for ind,m in enumerate(memory) if traversed[ind]]))
        if data[inst] == ">":
            index+=1
            inst+=1
        elif data[inst] == "<":
            index-=1
            inst+=1
        elif data[inst] == "+":
            memory[index] += 1
            if memory[index] > 255:
                memory[index] = 0
            inst+=1
        elif data[inst] == "-":
            memory[index] -= 1
            if memory[index] <= -1:
                memory[index] = 255
            inst+=1
        elif data[inst] == ".":
            if memory[index] == -1:
                print("EOF")
                break
            if verbose:
                output += chr(memory[index])
            else:
                print(chr(memory[index]),end="")
            
            inst+=1
        elif data[inst] == ",":
            memory[index] = ord(getch.getch())
            inst+=1
        elif data[inst] == "[":
            if memory[index] != 0:
                inst+=1
            else:
                loopstack.append(data[inst])
                while True:
                    inst+=1
                    if data[inst] == "[":
                        loopstack.append(data[inst])
                    elif data[inst] == "]":
                        if loopstack[-1] == "[":
                            loopstack.pop(-1)
                            if not loopstack:
                                break
        elif data[inst] == "]":
            if memory[index] != 0:
                loopstack.append(data[inst])
                while True:
                    inst-=1
                    if data[inst] == "]":
                        loopstack.append(data[inst])
                    elif data[inst] == "[":
                        if loopstack[-1] == "]":
                            loopstack.pop(-1)
                            if not loopstack:
                                break
            else:
                inst+=1
    raise Exception("EOF")
except Exception as e:
    print("")
    if verbose:
        print("Halt Reason:",e)
except KeyboardInterrupt:
    if verbose:
        print("Halt Reason: User Halted.")
if verbose:
    inst -= 1
    print("--Program Data--")
    print(data[:inst]+"("+data[inst]+")",end="")
    if inst < len(data):
        print(data[inst+1:])
    print("--End Program Data--")
    print("Last Memory Index:",index)
    print("--Memory State at Halt--")
    print(" ".join([str(m) if ind != index else "/"+str(m)+"\\" for ind,m in enumerate(memory) if traversed[ind]]))
    print("--End of traversed Memory--")
    print("Output at Halt: ", output)
