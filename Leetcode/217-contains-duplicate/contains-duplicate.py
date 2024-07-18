class Solution(object):
    def containsDuplicate(self, nums):
        return False if len(set(nums))==len(nums) else True
   
        