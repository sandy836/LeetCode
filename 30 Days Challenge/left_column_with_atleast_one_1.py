class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        global_ans = float('inf')
        for i in range(row):
            low, high = 0, col-1
            local_ans = float('inf')
            while low<=high:
                mid = (low+(high - low)//2)
                if binaryMatrix.get(i, mid) == 1:
                    local_ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            global_ans = min(global_ans, local_ans)
        if global_ans == float('inf'):
            global_ans  = -1
        return global_ans