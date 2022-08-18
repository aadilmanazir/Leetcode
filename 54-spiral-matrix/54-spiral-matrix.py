class Solution:
    import numpy as np
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        seen = [[0 for i in range(n)] for i in range(m)]
        
        direction = 'right'
        
        out = [matrix[0][0]]
        seen[0][0] = 1
        curr = (0, 0)
        curr_sum = 1
        while True:
            if curr_sum == m * n:
                return out

            if direction == 'right':
                nex = (curr[0], curr[1] + 1)
                if nex[1] >= n or seen[nex[0]][nex[1]] == 1:
                    direction = 'down'
                    continue
                    
            elif direction == 'down':
                nex = (curr[0] + 1, curr[1])
                if nex[0] >= m or seen[nex[0]][nex[1]] == 1:
                    direction = 'left'
                    continue

            elif direction == 'left':
                nex = (curr[0], curr[1] - 1)
                if nex[1] < 0 or seen[nex[0]][nex[1]] == 1:
                    direction = 'up'
                    continue

            elif direction == 'up':
                nex = (curr[0] - 1, curr[1])
                if nex[0] < 0 or seen[nex[0]][nex[1]] == 1:
                    direction = 'right'
                    continue
            
            
            out.append(matrix[nex[0]][nex[1]])
            seen[nex[0]][nex[1]] = 1
            curr = nex
            curr_sum += 1
