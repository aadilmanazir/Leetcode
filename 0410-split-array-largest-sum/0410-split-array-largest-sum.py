class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def solution(nums, i, k, sums, d):
            if (i, k) in d:
                return d[(i, k)]
            
            if k == 1:
                # print("i: ", i, "k: ", k)
                # print("val: ", sums[i])
                d[(i, k)] = sums[i]
                return sums[i]
            
            s = sums[i]
            goal = s/k
            curr_sum = nums[i]
            j = i
            
            while curr_sum < goal:
                j += 1
                curr_sum += nums[j]
                
            i1 = j
            i2 = j + 1
            i4 = j + 3
            res1 = max(sums[i] - sums[i1], solution(nums, i1, k-1, sums, d))
            if i2 < len(nums):
                res2 = max(sums[i] - sums[i2], solution(nums, i2, k-1, sums, d))
            else:
                res2 = float('inf')
            if i4 < len(nums):
                res4 = max(sums[i] - sums[i4], solution(nums, i4, k-1, sums, d))
            else:
                res4 = float('inf')
            
            res = min(res1, res2, res4)
            d[(i, k)] = res
            
            # print("i: ", i, "k: ", k)
            # print("i1: ", i1, "i2: ", i2, "res1: ", res1, "res2: ", res2)
            # print("d: ", d)
            return res        
        
        sums = []
        curr_sum = 0
        for x in nums[::-1]:
            curr_sum += x
            sums.append(curr_sum)
        
        sums.reverse()
        d = {}

        return solution(nums, 0, k, sums, d)
        
        