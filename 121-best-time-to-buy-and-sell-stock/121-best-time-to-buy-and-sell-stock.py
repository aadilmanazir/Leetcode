class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = float('-inf')
        l = []
        for i in range(len(prices) - 1):
            l.append(prices[i + 1] - prices[i])
        curr_sum = 0
        for x in l:
            curr_sum += x
            curr_max = max(curr_sum, curr_max)
            curr_sum = max(curr_sum, 0)
        return max(curr_max, 0)

        
            
        
        
        
        
        
        
        
        
        
        
        
        
        