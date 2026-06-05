"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        #sort the intervals
        intervals.sort(key = lambda x: x.start)
        prev_end = intervals[0].end
        for i in range(1,len(intervals)):
            current_start = intervals[i].start
            if current_start < prev_end:
                #current meeting overlaps with the previous one
                return False
            #update the prev_end with the current
            prev_end = intervals[i].end
        return True

