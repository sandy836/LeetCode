class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if self.isEmpty():
            self.stack.append((x,x))
        else:
            self.stack.append((x, min(self.stack[-1][1], x)))

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
    
    def isEmpty(self) -> bool:
        if not self.stack:
            return True
        return False
        