class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = global_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(local_max+nums[i], nums[i])
            global_max = max(global_max, local_max)
        
        return global_max