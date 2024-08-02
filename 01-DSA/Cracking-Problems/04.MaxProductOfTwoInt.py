# find the max product of two integers in the array where all elements are positive.
import numpy as np
arrayOne=np.array([1,20,30,40,50,60,55,34,54,66,98,45,33,45,4,3,6,10])
def findMaxProduct(array):
    maxProduct=0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j]>maxProduct:
                maxProduct=array[i]*array[j]
                pairs=str(array[i])+","+str(array[j])
    print(pairs)
    print(maxProduct)
findMaxProduct(arrayOne)

