class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(i, j, grid):
            grid[i][j] = 0
            if check(i + 1, j, grid) and grid[i+1][j] == "1":
                explore(i + 1, j, grid)
                
            if check(i, j + 1, grid) and grid[i][j+1] == "1":
                explore(i, j + 1, grid)
            
            if check(i - 1, j, grid) and grid[i-1][j] == "1":
                explore(i - 1, j, grid)
            
            if check(i, j - 1, grid) and grid[i][j-1] == "1":
                explore(i, j - 1, grid)
                
        def check(i, j, grid):
            m = len(grid)
            n = len(grid[0])
            return 0 <= i and i < m and 0 <= j and j < n
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    explore(i, j, grid)
                
        return res