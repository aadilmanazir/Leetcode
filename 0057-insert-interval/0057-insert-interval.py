class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        res = []
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        for x in intervals[1:]:
            if x[0] <= end:
                end = max(end, x[1])
            else:
                res.append([start, end])
                start = x[0]
                end = x[1]
                
        res.append([start, end])         
        return res
