class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        curr_start = intervals[0][0]
        curr_end = [intervals[0][1]]
        curr_min = 1
        for i, x in enumerate(intervals[1:]):
            for e in curr_end:
                if x[0] >= e:
                    curr_end.remove(e)
            curr_end.append(x[1])
            curr_min = max(curr_min, len(curr_end))
            
        return curr_min
        