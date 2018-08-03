#Write a function dups to find all duplicates in the list.

def Dubs(list1):
    n_list=[]
    j_list=[]
    for i in list1:
        if i not in n_list:
            n_list.append(i)
        else:
            j_list.append(i)
    print("Dublicate Elemets are :")
    print(j_list)

list1 = [1,2,3,4,5,6,7,1,3,6]
Dubs(list1)