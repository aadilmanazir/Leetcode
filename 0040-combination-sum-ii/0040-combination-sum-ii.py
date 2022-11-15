class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        s = set()
        counter = {}
        
        for c in candidates:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
                
        candidates = sorted(list(set(candidates)))    
        
        def helper(curr, i):
            total = sum(curr) if len(curr) >= 1 else 0
            
            if total == target:
                if tuple(curr) not in s:
                    res.append(curr)
                    s.add(tuple(curr))
                return
            
            if total > target or i >= len(candidates):
                return 
            
            c = candidates[i]
            for j in range(counter[c] + 1):
                curr_copy = curr[:]
                curr_copy += [c for k in range(j)]
                helper(curr_copy, i + 1)
        
        helper([], 0)
        return res