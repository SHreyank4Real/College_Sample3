#Write a program grep.py that takes a pattern and a filename as command-line argument and prints
#  all the lines in the file that contain given pattern

import io
import sys
import re

def GetName():
    #print("in GetName")
    if len(sys.argv) ==3:
        filename=sys.argv[1]
        patern=sys.argv[2]
        return filename,patern
    else:
        print("Exiting")
        exit()

def OpenFile(name):
    #print("in OpenFile")
    assert (name is not None)
    try:
        return (open(name))
    except FileNotFoundError:
        print("File not found")
        sys.exit()

def ReadLines(fobj):
    #print("in ReadLines")
    assert (fobj is not None)
    return fobj.readlines()

def FileClose(fobj):
    #print("in FileCLose")
    assert  (fobj is not None)
    fobj.close()

def test_patern():
    fname,patern = GetName()
    fdist = OpenFile(fname)
    lists = ReadLines(fdist)
    FileClose(fdist)
    #print("in test_patern")
    MatchPatern(patern,lists)

def MatchPatern(pat,lis):
    #print("MatchPatern")
    assert (pat is not None and lis is not None)
    for line in lis:
        if pat in line:
           print(line)

test_patern()
