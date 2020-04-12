class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []
        for char in S:
            if char != '#':
                stack_s.append(char)
            elif len(stack_s) != 0:
                stack_s.pop()
        
        for char in T:
            if char != '#':
                stack_t.append(char)
            elif len(stack_t) != 0:
                stack_t.pop()
        
        return ''.join(stack_t) == ''.join(stack_s)