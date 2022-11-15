class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]
        
        answer = self.subsets(nums[1:])
        res = []
        for a in answer:
            res += [a, [nums[0]] + a]
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        