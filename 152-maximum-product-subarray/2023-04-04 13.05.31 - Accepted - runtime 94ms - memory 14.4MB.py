class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0] # max from previous iteration
        prev_min = nums[0] # min from previous iteration
        max_to_n = nums[0] # max this iteration
        min_to_n = nums[0] # min this iteration
        ans = nums[0]
        
        # use previous max/min*current i or restart from i. The absolute value of the min could be larger so we store it.
        for n in nums[1:]:
            max_to_n = max(prev_max*n, prev_min*n, n)
            min_to_n = min(prev_max*n, prev_min*n, n)
            prev_max = max_to_n
            prev_min = min_to_n
            ans = max(ans, max_to_n)
        return ans