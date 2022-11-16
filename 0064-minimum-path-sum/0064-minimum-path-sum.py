class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for j in range(len(grid[0]))] for i in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) -1, -1, -1):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    continue
                res = float('inf')
                if j + 1 < len(grid[0]):
                    res = min(res, dp[i][j+1] + grid[i][j])
                if i + 1 < len(grid):
                    res = min(res, dp[i+1][j] + grid[i][j])
                dp[i][j] = res
                
        return dp[0][0]