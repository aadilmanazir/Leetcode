class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates, target):
            if candidates == []:
                return []
            
            if candidates[0] > target:
                return []
            
            elif candidates[0] == target:
                return [[candidates[0]]]
            
            if len(candidates) == 1:
                if target % candidates[0] == 0:
                    return [[candidates[0] for i in range(target//candidates[0])]]
                return []
            
            answer = []
            first = [[candidates[0]] + x for x in helper(candidates, target - candidates[0])]
            second = helper(candidates[1:], target)
            
            return first + second
        
        candidates.sort()
        return helper(candidates, target)
            
            
            
            
        
        
        
        
        
        
        