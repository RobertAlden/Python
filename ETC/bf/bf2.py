#!/usr/bin/env python3.10

import sys
import os.path
import re
import warnings

bf = re.compile('[\+\-\]\[\<\>\.\,]+')
# Define a filename.
filename = sys.argv[1]

if not os.path.isfile(filename):
    print('File does not exist.')
else:
    with open(filename) as f:
        data = "".join(f.readlines())

    if len(sys.argv) > 2:
        input_str = str(sys.argv[2])
    else:
        input_str = "0"
    inp_ptr = 0

    memory = [0] * 30000
    index = 0
    inst = 0
    loopstack = []
    data = "".join(data.split("\n"))
    data = bf.findall(data)
    data = "".join(data)
    inp_warned = False
    if len(re.findall('\[',data)) != len(re.findall('\[',data)):
        raise Exception("Mismatched brackets, verify input.")

    size = len(data)
    print(data)
    while inst < size-1:
        instruction = data[inst]
        print(instruction)
        match instruction:
            case ">":
                index+=1
            case "<":
                index-=1
            case "+":
                memory[index] += 1
                if memory[index] > 255:
                    memory[index] = 0
            case "-":
                memory[index] -= 1
                if memory[index] < -1:
                    memory[index] = 255
            case ".":
                if memory[index] == -1:
                    break
                print(chr(memory[index]),end="")
            case ",":
                memory[index] = ord(input_str[inp_ptr])
                inp_ptr = (inp_ptr + 1) % len(input_str)

                if not inp_warned and len(sys.argv) < 3:
                    inp_warned = True
                    warnings.warn("Warning:no input string declared, using 0's")
            case "[":
                if memory[index]:
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
            case "]":
                if not memory[index]:
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
        inst+=1
print("\nEOF")