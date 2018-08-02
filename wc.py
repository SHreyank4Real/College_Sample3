#Write a program wc.py that takes filename as argument and counts
#number of lines, words and chars in file

import sys

def Getname():
    if len(sys.argv) == 2:
        name = sys.argv[1]
        return name
    else:
        print("Program will exit now ")
        exit()

def Counting(name):
    num_letters,num_lines,num_words = 0,0,0
    fp = open(name,'r')
    #lines = fp.read()


    for line in fp:
        print(line)
        word = line.split(' ')

        num_letters +=len(line)
        num_words +=len(word)
        num_lines =num_lines+1

    print("Number of letters :",num_letters)
    print("Number of Words   :",num_words)
    print("NUmber of Lines   :",num_lines)
    fp.close()

Counting(Getname())