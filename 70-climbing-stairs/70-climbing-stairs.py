class Solution:
    def climbStairs(self, n: int) -> int:
        n = n + 1
        dp = [0] * n
        dp[-1] = 1
        for i in range(n - 2, -1, -1):
            one = i + 1
            two = i + 2
            if i == n - 2:
                dp[i] = dp[one]
            else:
                dp[i] = dp[one] + dp[two]
                
        return dp[0]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            