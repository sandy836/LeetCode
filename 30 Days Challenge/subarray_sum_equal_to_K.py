class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_count = dict()
        sum_count[0] = 1
        count = cum_sum = 0
        for num in nums:
            cum_sum += num
            if cum_sum-k in sum_count:
                count += sum_count[cum_sum-k]
            sum_count[cum_sum] = sum_count.get(cum_sum, 0) + 1
        return count