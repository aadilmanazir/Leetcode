class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        curr_max = (right - left) * min(height[left], height[right])
        while left != right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
            curr_max = max((right - left) * min(height[left], height[right]), curr_max)
        return curr_max