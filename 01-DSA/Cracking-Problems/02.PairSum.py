# find two pairs for making the result of target value.
def findPairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                continue
            if nums[i]+nums[j]==target:
                print(i,j)
listOne=[1,2,3,3,2,1,4,5,5,3,2]
findPairs(listOne,6)
