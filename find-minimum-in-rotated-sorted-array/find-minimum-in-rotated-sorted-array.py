class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return min(nums)
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        mid = nums[len(nums)//2]
        
        
        if mid >= nums[0]:
            return self.findMin(nums[len(nums)//2:])
        else:
            return self.findMin(nums[:len(nums)//2 + 1])