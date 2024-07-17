class Solution(object):
    def majorityElement(self, nums):
        element=None
        counts=0
        for num in nums:
            if counts ==0:
                element=num
            counts+=1 if element ==num else -1
        return element
        