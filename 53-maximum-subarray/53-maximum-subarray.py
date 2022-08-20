class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 0
        curr_max = nums[0]
        for i in range(n):
            curr += nums[i]
            curr_max = max(curr_max, curr)
            if curr < 0:
                curr = 0
                
        return curr_max
    
        
        
        
        
        
        
        
        
        