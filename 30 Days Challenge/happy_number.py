class Solution(object):
    def isHappy(self, n):
        while (n!=1):
            _sum = 0
            while n != 0:
                digit = n%10
                _sum += digit**2
                n = n//10
            if _sum == 4:
                return False
            n = _sum
        return True