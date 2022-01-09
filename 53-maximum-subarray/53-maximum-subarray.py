class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        curr_max = nums[0]
        for num in nums[1:]:
            curr = max(num, curr + num)
            curr_max = max(curr_max, curr)
        
        return curr_max
    
        
        
        
        
        
        
        
        
        