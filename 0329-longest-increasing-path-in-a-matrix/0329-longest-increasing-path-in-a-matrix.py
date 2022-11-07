class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def helper(matrix, d, i, j):
            if (i, j) in d:
                return d[(i, j)]
            
            v = matrix[i][j]
            curr_max = 0
            
            if i > 0 and matrix[i-1][j] > v:
                curr_max = max(curr_max, helper(matrix, d, i-1, j))
                
            if j > 0 and matrix[i][j-1] > v:
                curr_max = max(curr_max, helper(matrix, d, i, j-1))
                
            if i < len(matrix) - 1 and matrix[i+1][j] > v:
                curr_max = max(curr_max, helper(matrix, d, i+1, j))
                
            if j < len(matrix[0]) - 1 and matrix[i][j+1] > v:
                curr_max = max(curr_max, helper(matrix, d, i, j+1))            
                    
            d[(i, j)] = curr_max + 1
            return d[(i, j)] 
        
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                helper(matrix, d, i, j)
                
        return max(d.values())
            