class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                dp[i] = dp[i+1] + cost[i]
            else:
                dp[i] = cost[i] + min(dp[i+1], dp[i + 2])
                
        return min(dp[0], dp[1])
                
                
            
            
            
            
            
            
            
        