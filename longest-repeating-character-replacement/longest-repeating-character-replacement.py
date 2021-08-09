class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        left = 0
        right = 0
        curr_max = 0
        res = 0
        
        for right in range(len(s)):
            if s[right] not in d:
                d[s[right]] = 1
                curr_max = max(curr_max, 1)
                
            else:
                d[s[right]] += 1
                curr_max = max(curr_max, d[s[right]])
            
            if curr_max + k >= right - left + 1:
                res = max(res, right - left + 1)
                continue
                
            while curr_max + k < right - left + 1:
                d[s[left]] -= 1
                curr_max = max(d.values())                            
                left += 1
                
        return res
                
                
                
            
                
            
            
            
        
        
        
        