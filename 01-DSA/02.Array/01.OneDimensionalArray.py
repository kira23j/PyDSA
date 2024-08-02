# create and insert an element.
from array import *
arr_one=array('i',[1,2,3])

ins=int(input("please insert the array value: "))
ind=int(input("please insert the index value for new element "))
arr_one.insert(ins,ind)
print(arr_one)

# traverse through an array
def traverse(array):
    for i in array:
        print(i)
traverse(arr_one)
# has a time complexity of o<n>

# accssing an element
arr1=array('i',[1,2,3,4,5])
def accessElement(array,index):
    if index>len(array):
        print("there is no element in the index")
    else:
        print(array[index])
accessElement(arr1,7)

# Searching for element.
def searchInArray(array,value):
    for i in array:
        if i==value:
            return array.index(value)
    return "the element doesnt exist in this array"
print("the final output is: ",searchInArray(arr1,3))
# this will print 2


arr1=array('i',[1,2,3,4,5,6])
print(f"arr1= {arr1}")
# deleting an element
# remove from end has time complexity o(1)
arr1.remove(6)
#  remove from middle will take o(n) complexity
arr1.remove(4)
print(f"after removing arr1: we have left {arr1}")