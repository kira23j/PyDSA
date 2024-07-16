class Solution(object):
    def characterReplacement(self, s, k):
        left=right=0
        max_len=0
        majority=0
        counts=defaultdict(int)
        while right<len(s):
            counts[s[right]]+=1
            majority=max(majority,counts[s[right]])
            while majority+k<right - left + 1:
                counts[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
            right +=1
        return max_len

        
        