class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        length = len(s)
        for rotate_type, amount in shift:
            amount = amount%length
            if rotate_type == 1:
                amount = length-amount
            s = s[amount:]+s[0:amount]
        return s