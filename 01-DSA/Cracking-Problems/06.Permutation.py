# check if two lists are permutation of each other
list_one=[1,2,3]
list_two=[3,2,1]
def Permutation(list1,list2):
    if len(list1)!=len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False
print(Permutation(list_one,list_two))