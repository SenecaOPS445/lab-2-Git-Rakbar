#!/usr/bin/env python3
#Author: Rayhan Akbar
#Author ID: rakbar8
#Date created: 2024/05/23

import sys


#timer = int(sys.argv[1])

#print(sys.argv[0])

# completely skips this if block with all operators
if len(sys.argv) <= 1:
    timer = 3
    while timer != 0:
        print(timer)
        timer = timer - 1

# and never skips else block because ^^ 
else:
    timer = int(sys.argv[1])
    while timer != 0:
        print(timer)
        timer = timer - 1

#    break
#while timer == 0:
#   print(timer)
#   print("blast off!")
#    break

print("blast off!")