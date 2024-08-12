class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        s_dict={}
        for char in s:
            s_dict[char]=s_dict.get(char,0)+1
        for char in t:
            s_dict[char]=s_dict.get(char,0)-1
            if s_dict[char]<0:
                return False
        return True
        