#Write a program head.py that takes a filename as command-line argument and prints the
#first 5 lines of it.

import sys

def Getname():
    if len(sys.argv) == 2:
        name = sys.argv[1]
        return name
    else:
        print("Program will exit now ")
        exit()

def PrintFive(name):
    fp = open(name,'r')
    for i in range(0,5):
        text=fp.readline()
        print(text,end='')
    fp.close()

PrintFive(Getname())