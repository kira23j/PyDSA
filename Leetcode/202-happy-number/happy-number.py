class Solution(object):
    def calc(self, n):
        cur=0
        while n>0:
             digit=n%10
             cur+=digit*digit
             n//=10
        return cur
    def isHappy(self , n):
        seen=set()
        while n!=1:
            n=self.calc(n)
            if n in seen:
                return False
            seen.add(n)
        return True



        