class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            # even case
            res+=self.helper(s, i, i+1)
            # odd case
            res+=self.helper(s, i, i)

        return res

    def helper(self, s, l, r):
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1
            l-=1
            r+=1
        return res