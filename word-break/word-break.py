class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s))]
        dp.append(True)
        for i in range(len(s) - 1, -1, -1):
            yes = False
            for w in wordDict:
                if len(s[i:]) >= len(w):
                    if dp[i + len(w)] and s[i:i + len(w)] == w:
                        dp[i] = True
                        yes = True
                        break
            if yes:
                continue
                        
            dp[i] = False
            
        return dp[0]
        
        
        
        
        
        
        