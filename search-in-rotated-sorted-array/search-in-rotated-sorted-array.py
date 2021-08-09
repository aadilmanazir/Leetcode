class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target):
            if nums == []:
                return -1
            elif len(nums) <= 3:
                for i, x in enumerate(nums):
                    if x == target:
                        return i
                return -1

            mid = len(nums)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                res = binary_search(nums[:mid + 1], target)
                return res
            
            else:
                res = binary_search(nums[mid:], target)
                if res == -1:
                    return -1
                return mid + res
        
        def smallest_index(nums):            
            if len(nums) <= 3:
                small = min(nums)
                for i, x in enumerate(nums):
                    if x == small:
                        return i
             
            if nums[0] <= nums[-1]:
                return 0
            mid = len(nums)//2
            if nums[mid] >= nums[0]:
                return mid + smallest_index(nums[mid:])
            else:
                return smallest_index(nums[:mid + 1])
            
        i = smallest_index(nums)
        
        a = nums[:i]
        b = nums[i:]
        a_res = binary_search(a, target)
        b_res = binary_search(b, target)
        
        if b_res != -1:
            b_res += i
            
        return max(a_res, b_res)
            
            

        
        
        
        
            
            
        