class Solution:
    def rob(self, nums: List[int]) -> int: 
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[n - 1] = nums[n - 1]
        
        for i in range(n - 2, -1, -1):
            if i == n - 2:
                dp[i] = nums[i] 
                
            else:
                dp[i] = nums[i] + max(dp[i + 1] - nums[i + 1], dp[i + 2])
                
        return max(dp[0], dp[1])
            
            
            
            
            
            
            
         
        
        
        
        
        
        
        
        
        