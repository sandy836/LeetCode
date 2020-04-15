class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_product = [1]*length
        right_product = [1]*length
        for i in range(1, length):
            left_product[i] = left_product[i-1]*nums[i-1]
        
        right_product = 1
        for i in range(length-1, -1, -1):
            left_product[i] = left_product[i]*right_product
            right_product *= nums[i]
        return left_product