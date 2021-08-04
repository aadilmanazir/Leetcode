class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        answer = nums[0]
        
        for i in range(1, len(nums)):
            answer = max(answer, nums[i], curr_max * nums[i], curr_min * nums[i])
            temp_max = max(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_min = min(nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_max = temp_max
        
        return answer
        
        
        
        
         