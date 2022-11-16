class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for j in range(len(grid[0]))] for i in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        
        def helper(dp, i, j):
            if i >= len(grid) or j >= len(grid[0]):
                return
            elif dp[i][j] < float('inf'):
                return
            helper(dp, i+1, j)
            helper(dp, i, j+1)
            if i + 1 < len(grid):
                dp[i][j] = min(dp[i][j], grid[i][j] + dp[i+1][j])
            if j + 1 < len(grid[0]):
                dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j+1])
                
        helper(dp, 0, 0)        
        return dp[0][0]