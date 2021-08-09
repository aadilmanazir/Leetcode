class Solution:
    def numDecodings(self, s: str) -> int:
        double = {'10', '11', '12', '13', '14', '15',
                 '16', '17', '18','19', '20', 
                  '21', '22', '23', '24', '25', '26'}
        
        n = len(s)
        dp = [0] * n
        dp.append(1)
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                if s[i] != '0':
                    dp[i] += 1                  
            else:
                if s[i] != '0':
                    dp[i] += dp[i+1]
                    if s[i:i+2] in double:
                        dp[i] += dp[i+2]
                        
                        
        return dp[0]
                
        
        
        
        
        
        
        