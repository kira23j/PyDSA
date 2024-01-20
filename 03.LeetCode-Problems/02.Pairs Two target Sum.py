# write a program to find the index for which the sum
# of target number is satisified.
def findPairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                continue
            elif nums[i]+nums[j]==target:
                print(i,j)
my_list=[1,2,3,2,3,4,5,6]
findPairs(my_list,6)