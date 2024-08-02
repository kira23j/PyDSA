import numpy as np
# lets check if the number exist in array.
myArray=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
def findNumber(array,number):
    for i in range(len(array)):
        if array[i]==number:
            print(i, "is on the list")
findNumber(myArray,13)
findNumber(myArray,34)