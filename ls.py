#Write a program ls.py that takes path to a directory as command-line argument and prints all the
#files in that directory. When no argument is specified, it should list the files in the current
#directory

import sys
import os

def GetPath():
    if len(sys.argv) == 2:
        return sys.argv[1]
    else:
        return os.getcwd()

def PrintFiles():
    path = GetPath()
    Display(path)

def Display(path):
    print("Files are :")
    flist = os.listdir(os.chdir(path))
    for file in flist:
        if os.path.isfile(file):
            print(file)

PrintFiles()