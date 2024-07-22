class Solution(object):
    def findTheDifference(self, s, t):
        sum=0
        for i in t:
            sum+=ord(i)
        for i in s:
            sum-=ord(i)
        return chr(sum)
        