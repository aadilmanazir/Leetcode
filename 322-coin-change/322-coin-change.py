class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * amount
        dp = [0] + dp
        for i in range(len(dp)):
            if i in coins:
                dp[i] = 1
                
            else:
                for c in coins:
                    if i - c > 0:
                        dp[i] = min(1 + dp[i - c], dp[i])
                        
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]