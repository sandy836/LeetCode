class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0]*(col+1) for _ in range(row+1)]
        max_side_length = 0
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    continue
                dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1])+1
                max_side_length = max(max_side_length, dp[i+1][j+1])
        
        return max_side_length*max_side_length