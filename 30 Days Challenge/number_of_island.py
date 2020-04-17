class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i,j,grid)
                    count += 1
        return count
                
    def dfs(self, x, y, grid):
        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y] != '1':
            return 
        grid[x][y] = '#'
        self.dfs(x-1,y, grid)
        self.dfs(x+1,y, grid)
        self.dfs(x,y-1, grid)
        self.dfs(x,y+1, grid)