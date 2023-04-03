class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case, if the input array is only one element we do not want to skip the element and skip it due to list slicing. 
        if len(nums)==1:
            return nums[0]
        else:
            return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2= 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(rob2, rob1+n)
        return rob2