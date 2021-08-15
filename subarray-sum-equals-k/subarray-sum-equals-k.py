class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c_sum = {0: 1}
        curr = 0
        counter = 0
        for x in nums:
            curr += x
            if curr - k in c_sum:
                counter += c_sum[curr - k]
                
            if curr in c_sum:
                c_sum[curr] += 1
                
            else:
                c_sum[curr] = 1
                
        return counter 
        
        