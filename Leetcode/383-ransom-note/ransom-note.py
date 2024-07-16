class Solution(object):
    def canConstruct(self, ransomNote, magazine):
      d=defaultdict(int)
      for char in magazine:
        d[char]+=1
      for char in ransomNote:
        if char not in d or d[char]<=0:
            return False
        d[char]-=1
      return True
        