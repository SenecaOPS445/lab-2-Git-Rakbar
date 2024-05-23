#!/usr/bin/env python3
import sys


if len(sys.argv) <= 1:
    print("Usage: " + sys.argv[0]+ " name age")
    sys.exit()

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0]+ " name age")
    sys.exit()


name = sys.argv[1]
age = sys.argv[2]

#print('Hi ' + name + ', you are ' + str(age) + ' years old.')

#colour = input("Type in a colour and press enter: ")
#print('The colour I typed in is: ' + colour)


print('Hi ' + name + ', you are ' + str(age) + ' years old.')