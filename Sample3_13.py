#Write a function unique to find all the unique elements of a list

def BeUnique(list1):
    n_list=[]
    j_list=[]
    count =0
    for i in list1:
        count+=1
        if i not in n_list:
            n_list.append(i)
        else:
            j_list.append(i) #contains dublicate elements

    #prints only unique
    for i in j_list:
        n_list.remove(i)
    print(n_list)

list1 = [1,2,3,4,5,6,7,1,3,6]
BeUnique(list1)
