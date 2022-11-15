class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        
        for s in range(amount + 1):
            for c in coins:
                if s - c >= 0:
                    dp[s] = min(dp[s], dp[s - c] + 1)
                    
        return dp[-1] if dp[-1] < float('inf') else -1