class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1e4] * n
        dp[-1] = 0
        for i in range(n-2, -1, -1):
            j = nums[i]
            if j <= 0:
                continue

            curr_min = 1e4
            for k in range(i + 1, min(i + j + 1, n)):
                curr_min = min(curr_min, dp[k] + 1)
            dp[i] = curr_min
        return dp[0]
        
        
        
        
        
        
        
        
        
        
        