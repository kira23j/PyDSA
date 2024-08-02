import numpy as np

twodarray=np.array([[1,2,3,4],[4,3,2,1],[5,4,3,2]])
print(twodarray)

# adding a row,axis=0 and column ,axis=1
new2dArray=np.insert(twodarray,0,[[1,2,4]],axis=1)
print(new2dArray)
# use append to add at the end
anotherOne=np.append(new2dArray,[[1,2,3,4,5]],axis=0)
print(anotherOne)
# accessing elements in 2d array
def accessElement(array,rowIndex,colIndex):
    """for accessing elements from 2d array"""
    if rowIndex>=len(array) and colIndex>=len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])

print(accessElement(twodarray,2,2))
# traversing the elements in array:

def traverseArray(array):
    for i in  range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
            
print(traverseArray(twodarray))
            
        # searching for value in a 2d array
def search2dArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]==value:
                return "The value is located at index"+str(i)+" "+str(j)
            return "The element is not found"

print(search2dArray(twodarray,4))      

# deleting an element form 2d array using numpy, delete first column
delArray=np.delete(twodarray,0,axis=1)
print(delArray)
# deleting first row
delArray=np.delete(twodarray,0,axis=0)
print(delArray)