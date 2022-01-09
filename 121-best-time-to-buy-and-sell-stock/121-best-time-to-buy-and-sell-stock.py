class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Kadane's algorithm
        if len(prices) <= 1:
            return 0
        diff = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        curr_max = float('-inf')
        curr = 0
        for num in diff:
            curr += num
            if curr < 0:
                curr = 0
            curr_max = max(curr, curr_max)
        return curr_max
            
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        