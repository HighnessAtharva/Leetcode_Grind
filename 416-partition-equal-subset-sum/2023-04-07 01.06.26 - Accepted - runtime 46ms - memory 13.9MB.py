class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: 
            return False
        s, dp = s // 2, 1
        for n in nums:
            dp |= dp << n
        return dp & 1 << s