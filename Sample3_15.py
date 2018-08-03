#Write a function group(list, size) that take a list and splits into smaller lists of given size.

import random

def group(list,size):
    lis1,lis2=[],[]
    for i in range(0,size):
        #print(list[i])
        lis1.append(list[i])
    for i in range(size, len(list)):
        lis2.append(list[i])
    print(lis1)
    print(lis2)


def get_list():
    num = int(input('Enter the origenal list size :'))
    ori_list = []
    for i in range(num):
        ori_list.append(random.randint(10,100))
    print(ori_list)
    split_list(ori_list)

def split_list(ori_list):
    size = int(input("Enter the size to split :"))
    group(ori_list,size)

get_list()

