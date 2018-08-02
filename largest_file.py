#Write a program largest-file.py to find the largest file in the given directory. The program
# should accept the directory name as command-line argument and print path to the file
# (not just filename).

import sys
import os

def GetDName():
    if len(sys.argv) == 2:
            return sys.argv[1]
    else:
        print("Exiting")
        exit()

def FindLarge():
    dname = GetDName()
    flist = os.listdir(dname)
    big = 0
    name,cname ='',''

    for i in flist:
        if os.path.getsize(i) > big:
            big = os.path.getsize(i)
            name = i
            cname = os.getcwd()
    print(name)
    print(cname)

FindLarge()