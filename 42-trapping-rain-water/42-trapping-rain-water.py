class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        
        curr_max = 0
        for h in height:
            left.append(curr_max)
            curr_max = max(curr_max, h)
            
        curr_max = 0
        for h in height[::-1]:
            right.append(curr_max)
            curr_max = max(curr_max, h)    
            
        
        right.reverse()
        answer = 0
        for i, h in enumerate(height):
            answer += max(0, min(left[i], right[i]) - h)
        return answer
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        