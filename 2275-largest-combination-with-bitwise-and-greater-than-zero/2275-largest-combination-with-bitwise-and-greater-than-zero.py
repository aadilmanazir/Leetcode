class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        l = []
        for i in range(len(candidates)):
            l.append((i, '{0:025b}'.format(candidates[i])))
        
        curr_max = 0

        for i in range(25):
            count = 0
            for j in range(len(l)):
                if l[j][1][i] == "1":
                    count += 1
                    
            curr_max = max(curr_max, count)
        return curr_max
        
        