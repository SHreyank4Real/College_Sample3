#Write a program copyfile.py to copy one file to another. It should accept two filenames as
#command-line arguments and copies the first one into the second
import sys

def GetFile():
    if len(sys.argv) ==3:
        copy=sys.argv[1]
        paste=sys.argv[2]
        return copy,paste
    else:
        print("Exiting")
        exit()
def Copying():
    try:
        copy,paste=GetFile()
        cp = open(copy,'r')
        pp = open(paste,'w')

        texts = cp.read()
        pp.write(texts)
        print("file copied")
    except IOError:
        print("File not copied")

Copying()
