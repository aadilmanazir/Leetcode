class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        answer = 0
        for x in s:
            if x - 1 not in s:
                counter = 0
                a = x
                while a in s:
                    counter += 1
                    a += 1
                answer = max(answer, counter)
                    
        return answer
                
            