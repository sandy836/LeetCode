class FirstUnique:
    def __init__(self, nums: List[int]):
        self.hash = {}
        self.queue= []
        for num in nums:
            self.add(num)
            
    def showFirstUnique(self) -> int:
        while self.queue and self.hash[self.queue[0]]>1:
            self.queue.pop(0)
        if not self.queue:
            return -1
        return self.queue[0]
            
    def add(self, value: int) -> None:
        self.queue.append(value)
        self.hash[value] = self.hash.get(value, 0)+1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)