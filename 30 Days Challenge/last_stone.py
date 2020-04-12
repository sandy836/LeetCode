import heapq 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            smash = heapq.heappop(stones) - heapq.heappop(stones)
            heapq.heappush(stones,smash)
        
        return -1*heapq.heappop(stones)