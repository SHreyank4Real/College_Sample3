#Write a program sumfile.py that takes a filename as argument and prints sum of all numbers in
# that file. It is assumed that the file will only have one number  in every line.
import sys

def Getname():
    if len(sys.argv) == 2:
        name = sys.argv[1]
        return name
    else:
        print("Program will exit now ")
        exit()

def NumCount(name):
    fp = open(name,'r')
    lines = fp.read()
    num = 0
    for line in lines:
        if line.isnumeric():
            num +=1

    fp.close()
    print("Number of numbers in file is :",num)

NumCount(Getname())

