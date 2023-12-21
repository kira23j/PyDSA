from array import *
arr_one=array('i',[1,2,3])

ins=int(input("please insert the array value"))
ind=int(input("please insert the index value for new element."))
arr_one.insert(ins,ind)
print(arr_one)