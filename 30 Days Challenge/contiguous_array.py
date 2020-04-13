class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum_index = dict()
        prefix_sum_index[0] = 0
        _sum = gloabl_max = 0
        for i in range(0, len(nums)):
            _sum += -1 if nums[i] == 0 else 1
            if _sum in prefix_sum_index:
                gloabl_max = max(gloabl_max, i-prefix_sum_index[_sum]+1)
            else:
                prefix_sum_index[_sum] = i+1
        return gloabl_max