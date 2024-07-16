class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        for i in range(len(nums)):
            if nums[i] in d and i-d[nums[i]] <=k:
                return True
            d[nums[i]]=i
        return False
       
        