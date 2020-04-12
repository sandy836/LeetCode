class Solution(object):
    def moveZeroes(self, num):
        last_zero_index = 0
        for i in range(0, len(num)):
            if num[i] != 0:
                temp = num[last_zero_index]
                num[last_zero_index] = num[i]
                num[i] = temp
                last_zero_index += 1
        return num