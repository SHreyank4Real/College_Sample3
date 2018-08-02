#Write a program cat.py that takes a filename as command-line argument and prints all the contents of that file.
import sys
import io

def Getname():
    if len(sys.argv) == 2:
        name = sys.argv[1]
        return name
    else:
        print("Program will exit now ")
        exit()

def Printing(name):
    try:
        fp = open(name,'r')
        lines = fp.read()
        print(lines)
    except FileNotFoundError:
        print("File not exists!")
        exit()

Printing(Getname())