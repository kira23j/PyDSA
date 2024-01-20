# how to find the missing number in an integer array of a and b lets say for this case 1-10
# sum of 1 upto n=n*n+1/2
# so in this example 4 is missing

myList=1,2,3,5,6,7,8,9,10
def findMissing(List,n):
    sumOne=10*11/2
    sumTwo=sum(List)
    print(sumOne-sumTwo)
findMissing(myList,10)