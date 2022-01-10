class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        counter = 0 
        for x in intervals[1:]:
            if x[0] < curr_end:
                if x[1] < curr_end:
                    curr_start = x[0]
                    curr_end = x[1]
                counter += 1
            else:
                curr_start = x[0]
                curr_end = x[1]
        return counter