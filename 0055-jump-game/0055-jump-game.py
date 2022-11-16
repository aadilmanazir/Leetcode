class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            jump = False
            for j in range(i, min(nums[i] + i + 1, len(nums))):
                if dp[j]:
                    jump = True
                    break
            dp[i] = jump
            
        return dp[0]