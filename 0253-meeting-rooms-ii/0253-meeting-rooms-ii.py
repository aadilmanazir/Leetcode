class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        end = [intervals[0][1]]
        res = 1
        for x in intervals[1:]:
            new_end = []
            for e in end:
                if e > x[0]:
                    new_end.append(e)
            new_end.append(x[1])
            end = new_end
            res = max(res, len(new_end))
                
        return res
                
        