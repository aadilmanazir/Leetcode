class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, target):
            left = 0
            right = len(l) - 1
            while left <= right:
                mid = (left + right)//2
                if l[mid] < target:
                    left = mid + 1
                elif l[mid] > target:
                    right = mid - 1
                else:
                    return mid
                
            return -1
        
        if nums[0] < nums[-1]:
            return binary_search(nums, target)
        
        if len(nums) <= 3:
            return nums.index(target) if target in nums else -1
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > nums[mid + 1]:
                left_bs = binary_search(nums[:mid+1], target)
                right_bs = binary_search(nums[mid+1:], target)
                if left_bs == -1 and right_bs == -1:
                    return -1
                if left_bs > -1:
                    return left_bs
                return right_bs + mid + 1
            
            if nums[mid] < nums[left]:
                right = mid -  1
            else:
                left = mid + 1
        
        
        
            
            
        